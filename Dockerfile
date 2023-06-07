# Pull base image
FROM python:3.9

# Create work directory
WORKDIR /usr/src/app

# Install poetry env, project dependency and model files
COPY poetry.lock pyproject.toml ./

# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir poetry==1.2.0 \
    && pip install --no-cache-dir --upgrade mxnet==1.9.1 \
    && pip install --no-cache-dir "torch==1.7.1+cpu" "torchvision==0.8.2+cpu" -f https://download.pytorch.org/whl/torch_stable.html \
    && pip install --no-cache-dir --upgrade gluoncv==0.10.5.post0 \
    && pip install --no-cache-dir decord==0.6.0 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev

# Copy application files
COPY ./ ./

# Expose port and run application
EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c", "uvicorn main:app --host 0.0.0.0"]
