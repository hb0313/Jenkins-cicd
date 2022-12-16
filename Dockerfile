# Pull base image
FROM python:3.9

# Create work directory
WORKDIR /usr/src/text-translation

#Install poetry env, project dependency and model files
COPY poetry.lock pyproject.toml ./

# hadolint ignore=DL3008,DL3007,DL3009
RUN apt-get update && apt-get install -y libsndfile1 ffmpeg \
    && apt install libsqlite3-dev \
    && apt-get install libbz2-dev;pip install --upgrade pip; pip install Cython; pip install nemo-toolkit["all"]
RUN pip install --no-cache-dir poetry==1.3.0
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

# Copy application files
COPY ./ ./

# Expose port and run application
EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c", "uvicorn main:app --host 0.0.0.0"]