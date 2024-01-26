# Utiliza una imagen de Python más ligera como base
FROM python:3.7-slim-buster

# Instalación de dependencias necesarias para Chrome/Chromedriver
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt-dev \
    gcc \
    build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/*

# Copiar los archivos del proyecto al contenedor
COPY . /app
WORKDIR /app

# Instalación de las dependencias de Python
RUN pip install -r requirements.txt

# Comando para ejecutar el script
CMD ["python", "registre_jornada/app.py"]
