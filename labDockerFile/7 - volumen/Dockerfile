#carga python
FROM python:3.10-slim
#Agrega esto a tu Dockerfile para instalar bash o sh
RUN apt-get update && apt-get install -y bash

#crea el dir, y a la vez se dice que todo se trabajara sobre el
WORKDIR /app
COPY app1.py .
COPY app2.py .
#crea un dir donde cuando ese ejcute el comando run
VOLUME ["/app/data"]
# se ejecuta solo y solo si, no hay mas argunemntos despues del run
CMD ["python", "app1.py"]