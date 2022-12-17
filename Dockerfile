# Pull base image
FROM nvcr.io/nvidia/pytorch:22.01-py3

# Create work directory
WORKDIR /usr/src/text-translation

#Install poetry env, project dependency and model files
COPY poetry.lock pyproject.toml ./

# hadolint ignore=DL3008,DL3007,DL3009
RUN pip install nemo_toolkit[all]
RUN pip install --no-cache-dir poetry==1.3.0 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy application files
COPY ./ ./

# Expose port and run application
EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c", "uvicorn main:app --host 0.0.0.0"]