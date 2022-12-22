ARG BASE_IMAGE=python:3.9-slim
FROM ${BASE_IMAGE} as nemo-deps

# Ensure apt-get won't prompt for selecting options
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y \
    libsndfile1 sox \
    libfreetype6 \
    swig \
    ffmpeg && \
    rm -rf /var/lib/apt/lists/*

#WORKDIR /tmp/

# copy nemo source into a scratch image
FROM scratch as nemo-src
COPY . .

# start building the final container
FROM nemo-deps as nemo
#ARG NEMO_VERSION=1.14.0


# Install NeMo
RUN from=nemo-src,target=/tmp/ cd /tmp/ && pip install Cython && pip install nemo_toolkit['all']


WORKDIR /workspace/nemo
COPY poetry.lock pyproject.toml ./
RUN pip install --no-cache-dir poetry==1.3.0 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi


# Copy application files
COPY ./ ./

# Expose port and run application
EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c", "uvicorn main:app --host 0.0.0.0"]
