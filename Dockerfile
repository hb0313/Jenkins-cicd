# Pull base image
FROM python:3.9

# Install Git LFS
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash \
    && apt-get --no-install-recommends -y install git-lfs=3.2.0

# Create work directory
WORKDIR /usr/src/vissl-regnet

#Install poetry env, project dependecny and model files
COPY poetry.lock pyproject.toml ./
RUN pip install --no-cache-dir poetry==1.1.11 && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
RUN git clone https://huggingface.co/facebook/regnet-y-040

#Copy files
COPY ./ ./

#Expose port and run application
EXPOSE 8000
ENTRYPOINT ["/bin/sh", "-c", "uvicorn main:app --host 0.0.0.0"]