# Pull base image
FROM nvcr.io/nvidia/pytorch:22.01-py3 AS builder

# Create work directory
WORKDIR /usr/src/text-translation

#Install poetry env, project dependency and model files
#COPY ./ ./

# hadolint ignore=DL3008,DL3007,DL3009
RUN pip install nemo_toolkit[all]


# Pull base image
FROM python:3.9

# Copy application files
COPY --from=builder /usr/src/text-translation ./

RUN pip install --no-cache-dir poetry==1.3.0 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Expose port and run application
EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c", "uvicorn main:app --host 0.0.0.0"]
