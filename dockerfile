FROM python:3.10.0-buster

WORKDIR /app
ENV PYTHONPATH /app/src

COPY poetry.lock ./
COPY pyproject.toml ./

RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y



RUN pip install poetry
RUN poetry install --no-interaction --no-ansi

COPY . .

CMD ["poetry", "run", "python", "src/main.py"]