import requests
import time
from datetime import datetime

while True:
    try:
        hora_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        r = requests.get("http://api:5000/")
        hora_respuesta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{hora_envio}] Enviado → [Cliente recibió]: {r.text} ← [{hora_respuesta}]")
    except Exception as e:
        hora_error = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{hora_error}] Esperando API... Error: {e}")
    time.sleep(3)
