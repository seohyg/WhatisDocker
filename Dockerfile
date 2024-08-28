FROM python:3.11-slim

WORKDIR /app

COPY test_docker.py .

ENV DOCKER_ENV_TEST="This is a Docker container"

CMD ["python", "test_docker.py"]