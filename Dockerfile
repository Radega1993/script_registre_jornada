FROM python:3.8
USER root
RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python registre_jornada/app.py
