FROM python:3.7-alpine

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .build-deps \
    gcc \
    build-base \
    libffi-dev \
    openssl-dev \
    libxml2-dev \
    libxslt-dev \
    chromium

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python registre_jornada/app.py
