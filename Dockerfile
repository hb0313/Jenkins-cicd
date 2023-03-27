# Pull base image
FROM python:3.9

# Create work directory
WORKDIR /usr/src/to-text-en-conformer-ctc-large-ls

#Install poetry env, project dependency and model files
COPY poetry.lock pyproject.toml ./

# hadolint ignore=DL3008,DL3007,DL3009,DL3006,DL3013,DL3042,DL3014,DL3015,DL3027
RUN  apt-get update &&  apt-get install --no-install-recommends -y libsndfile1 ffmpeg libsqlite3-dev libbz2-dev lzma liblzma-dev cmake; rm -rf /var/lib/apt/list/**;pip install Cython;pip install nemo_toolkit['all'];pip install --no-cache-dir poetry==1.2.0 && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy application files
COPY ./ ./

# Expose port and run application
EXPOSE 8000

# Define Entrypoint
ENTRYPOINT ["/bin/sh", "-c", "uvicorn main:app --host 0.0.0.0"]
