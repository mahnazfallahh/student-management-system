FROM python:latest

LABEL maitainer="mahnazfallah2023@gmail.com"

WORKDIR /src

COPY poetry.lock pyproject.toml /src/

RUN pip install poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /src

ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5432
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_DB=postgres

CMD ["python", "run.py"]





