# Imagen base (puede ser cualquier Linux ligero como Alpine o Debian)
# OBLIGATORIOOOO
FROM alpine:latest


# Crea un directorio dentro de la imagen
RUN mkdir /app

# Crea un archivo dentro del directorio
RUN echo "Esto es una archivo prueba" > /app/hola.txt


#soli se colocab muchos cmd, solo toma el ultimo
# Ejecuta varios comandos al iniciar el contenedor
CMD [ "sh", "-c", "ls /app && echo 'vamos a ver que trae el hola.txt' && cat /app/hola.txt" ]