FROM python:3.12-slim

WORKDIR /app

COPY ./src/docker_sample_app /app
COPY requirements.lock requirements.lock
COPY pyproject.toml pyproject.toml
COPY README.md README.md

RUN pip install -r requirements.lock

CMD ["python", "app.py"]
