FROM python:3.7-alpine

# Instalación de dependencias necesarias para Python y Chrome/Chromedriver
RUN apk add --update --no-cache \
    chromium \
    chromium-chromedriver \
    libffi-dev \
    openssl-dev \
    libxml2-dev \
    libxslt-dev \
    gcc \
    build-base

# Copiar los archivos del proyecto al contenedor
COPY . /app
WORKDIR /app

# Instalación de las dependencias de Python
RUN pip install -r requirements.txt

# Comando para ejecutar el script
CMD ["python", "registre_jornada/app.py"]
