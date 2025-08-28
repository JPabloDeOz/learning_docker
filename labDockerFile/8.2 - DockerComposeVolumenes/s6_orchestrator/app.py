from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

S1 = "http://s1_customer:8000/process"
S2 = "http://s2_pricing:8000/process"
S3 = "http://s3_inventory:8000/process"
S4 = "http://s4_token:8000/process"
S5 = "http://s5_ticket:8000/process"
S7 = "http://s7_compra:8000/save"
# S8 es lector, normalmente no lo llamamos desde s6, pero podría si quieres
S8 = "http://s8_reader:8000/read_tokens"

@app.get("/health")
def health():
    return jsonify(status="OK"), 200

@app.post("/run")
def run_pipeline():
    master = request.get_json(force=True)

    # 1) Servicios base
    r1 = requests.post(S1, json=master).json()
    r2 = requests.post(S2, json=master).json()
    r3 = requests.post(S3, json=master).json()

    # 2) Dependientes
    r4 = requests.post(S4, json=r1["data"]).json()
    r5 = requests.post(S5, json=r2["data"]).json()

    # 3) Nuevo servicio: guarda tickets en S7
    r7 = requests.post(S7, json=r5["data"]).json()

    # 4) Leer ticket con S8 usando el nombre que nos dio S7
    # Al final del pipeline, leer S8 con el id del request
# 4) Leer token con S8 usando el id del master
    r8 = requests.get(f"http://s8_reader:8000/read_tokens/{master.get('id')}").json()

    # 5) Ensamble final
    final = {
        "id": master.get("id"),
        "valid": r4["data"]["valid"],
        "token": r4["data"]["token"],
        "final_price": r2["data"]["final_price"],
        "moneda": r2["data"]["moneda"],
        "in_stock": r3["data"]["in_stock"],
        "ticket": r5["data"]["ticket"],
        "ticket_saved": r7.get("status") == "OK",
        "tokens_read_by_s8": r8.get("content", {}),  # <--- ya contiene el token leído desde S4
        "stock": r3["data"]["stock"],
        "message": "Venta aprobada" if (r4["data"]["valid"] and r3["data"]["in_stock"]) else "Venta pendiente o rechazada"
    }


    return jsonify(status="OK", result=final, steps={
        "s1_customer": r1,
        "s2_pricing": r2,
        "s3_inventory": r3,
        "s4_token": r4,
        "s5_ticket": r5,
        "s7_compra": r7,
        "s8_reader": r8
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
