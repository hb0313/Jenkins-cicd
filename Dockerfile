# Pull base image
FROM python:3.9

# Create work directory
WORKDIR /usr/src/text-to-speech-silero

#Install poetry env, project dependency and model files
# COPY poetry.lock pyproject.toml ./
# Copy application files
COPY ./ ./
RUN pip install --no-cache-dir poetry==1.4.0 && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi



# Expose port and run application
EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c", "uvicorn main:app --host 0.0.0.0"]
