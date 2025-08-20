FROM prueba3:2.0

# Crear un nuevo directorio
RUN mkdir /app/nuevo_dir

# Agregar un nuevo script
COPY nuevo.py /app/nuevo_dir/nuevo.py

# CMD final
CMD ["sh","-c","ls /app && ls /app/nuevo_dir && cat /app/holaMundo.py"]
