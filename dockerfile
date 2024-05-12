FROM python:3.10.0-slim

WORKDIR /app
ENV PYTHONPATH /app

COPY poetry.lock ./
COPY pyproject.toml ./

RUN pip install poetry
RUN poetry install --no-interaction --no-ansi

COPY . .

CMD ["poetry", "run", "python", "main.py"]