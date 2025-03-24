FROM gramep-image:latest

RUN mkdir -p /app/kmers
WORKDIR /app


# Set environment variable (optional)
ENV SOURCE=/app

CMD for variant in type1 type2 type3 type4; do \
        gramep get-only-kmers \
        --rpath "$SOURCE/refseq.fasta" \
        --spath "$SOURCE/$variant.fasta" \
        --save-path "$SOURCE/kmers/" \
        --word 6 \
        --step 1; \
        done