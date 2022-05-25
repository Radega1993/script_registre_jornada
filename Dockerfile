FROM python:3.8

RUN apt update && apt install -y gdebi-core libnss3 libgconf-2-4
ADD google-chrome-stable_current_amd64.deb .
RUN gdebi -n google-chrome-stable_current_amd64.deb

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

COPY chromedriver .
RUN chmod +x chromedriver

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "registre_jornada/app.py"]
