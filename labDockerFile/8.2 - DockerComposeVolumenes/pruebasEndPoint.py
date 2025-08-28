import requests

# URL del endpoint
url_process = "http://localhost:8000/process"  # Cambia esto si tu servidor está en otro puerto o dominio
url_healt = "http://localhost:8000/health"
url_principal = "http://localhost:8080/run"

# JSON que quieres enviar
payload_process = {
    "id": "123",
    "nombre": "Juan"
}
payload_process_principal = {
    "id": 123452,
    "nombre": "Juan",
    "edad": 30,
    "producto": "Laptop",
    "precio": 1200,
    "descuento": 10,
    "categoria": "Electrónica",
    "stock": 5,
    "pais": "MX",
    "moneda": "USD"
  }

try:
    #------------
    # Mostrar respuesta JSON
    #response_healt = requests.get(url_healt)
    # print("Código de estado:", response_healt.status_code, type(response_healt.status_code))
    # print("Respuesta JSON:", response_healt.json(), type(response_healt.json()))
    #-----------
    # Enviar POST con JSON
    # response_process = requests.post(url_process, json=payload_process)
    # print("Código de estado:", response_process.status_code, type(response_process.status_code))
    # print("Respuesta JSON:", response_process.json(), type(response_process.json()))
    #--------------
    response_principal = requests.post(url_principal,json=payload_process_principal)
    print("Código de estado:", response_principal.status_code, type(response_principal.status_code))
    print("Respuesta JSON:", response_principal.json(), type(response_principal.json()))

except requests.exceptions.ConnectionError as e:
    print("No se pudo conectar con el servidor.")
    print("Detalles del error:", e)

except requests.exceptions.Timeout as e:
    print("La conexión tardó demasiado y se agotó el tiempo.")
    print("Detalles del error:", e)

except requests.exceptions.HTTPError as err:
    print(f"Error HTTP: {err}")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    print("Detalles del error:", e)

