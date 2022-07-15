FROM python:3.10

# Poder leer los mensajes de la consola Python
ENV PYTHONUNBUFFERED 1

# Crear un directorio dentro del contenedor
RUN mkdir /code

# Definir directorio con el que vamos a trabajar
WORKDIR /code

# Copiamos el archivo requirements.txt al directorio principal
COPY requirements.txt /code/

# Instalamos las librerias necesarias del proyecto (asegurandonos que sea con la version de python + pip)
RUN python -m pip install -r requirements.txt

# Copiamos nuestro codigo al directorio principal
COPY . /code/