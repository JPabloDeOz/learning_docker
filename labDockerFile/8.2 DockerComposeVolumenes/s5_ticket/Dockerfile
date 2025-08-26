FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
COPY app.py .
#--no-cache-dir evita guardar archivos temporales de instalación → imagen más ligera
RUN pip install --no-cache-dir flask requests 
EXPOSE 8000
CMD ["python",  "-u","app.py"]