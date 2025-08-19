# En lugar de alpine, usa tu imagen ya creada
FROM prueba2:2.0  

# Ahora sí, construyes sobre lo que ya trae /app/hola.txt
COPY holaMundo.py /app/holaMundo.py

CMD ["sh", "-c", "ls /app && cat /app/holaMundo.py"]
