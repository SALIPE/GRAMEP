"""grid_search module.

This module contains the functions used to perform a grid search to suggest a value for
word and step size.

Contents:
    * grid_search: Perform grid search to suggest a value for word and step size.
"""
from thefuzz import fuzz
from thefuzz.process import dedupe

from gramep.data_io import buffer_sequences, load_sequences
from gramep.kmers_utils import kmers_difference
from gramep.messages import Messages

message = Messages()
"""
Set the Message class for logging.
"""


def grid_search(
    reference_path: str,
    sequence_path: str,
    min_word: int,
    max_word: int,
    min_step: int,
    max_step: int,
    dictonary: str = 'ACTG',
):
    """
    Perform grid search to suggest a value for word and step size.

    Args:
        reference_path (str): Path to reference sequence.
        sequence_path (str): Path to sequence.
        min_word (int): Min word size.
        max_word (int): Max word size.
        min_step (int): Min step size.
        max_step (int): Max step size.
        dictonary (str, optional): DNA dictionary. Defaults to 'ACTG'.

    Returns:
        Message class
    """
    sequences = buffer_sequences(sequence_path=sequence_path)
    reference = buffer_sequences(sequence_path=reference_path)

    selected_word = 0
    selected_step = 0
    selected_result = 0
    for word in range(min_word, max_word + 1):
        for step in range(min_step, max_step + 1):
            message.info_grid_running(word, step)
            seq_kmers = load_sequences(
                seq_records=sequences,
                word=word,
                step=step,
                dictonary=dictonary,
                reference=False,
            )
            ref_kmers = load_sequences(
                seq_records=reference,
                word=word,
                step=step,
                dictonary=dictonary,
                reference=True,
            )

            result = len(
                list(
                    dedupe(
                        kmers_difference(seq_kmers, ref_kmers),
                        threshold=70,
                        scorer=fuzz.ratio,
                    )
                )
            )

            if result > selected_result:
                selected_word = word
                selected_step = step
                selected_result = result

    message.info_selected_parameters(selected_word, selected_step)
    message.info_done()
