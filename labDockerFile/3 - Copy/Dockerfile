FROM alpine:latest

# Crear directorio
RUN mkdir /app

############# EJEMPLO 3

# Copiar holaMundo.py al contenedor
COPY holaMundo.py /app/holaMundo.py

# Comando que se ejecuta al iniciar el contenedor
CMD ["sh","-c","ls /app && cat /app/holaMundo.py"]
