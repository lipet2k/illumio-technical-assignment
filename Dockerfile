FROM python:3.11-slim-bookworm

WORKDIR /code
COPY . /code/

WORKDIR /code/src
CMD ["python3", "app.py"]