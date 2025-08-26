from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

S1 = "http://s1_customer:8000/process"
S2 = "http://s2_pricing:8000/process"
S3 = "http://s3_inventory:8000/process"
S4 = "http://s4_token:8000/process"
S5 = "http://s5_ticket:8000/process"

@app.get("/health")
def health():
    return jsonify(status="OK"), 200

@app.post("/run")
def run_pipeline():
    master = request.get_json(force=True)

    # 1) Servicios base
    r1 = requests.post(S1, json=master).json()   # -> {status, data:{id,nombre,valid}}
    r2 = requests.post(S2, json=master).json()   # -> {status, data:{id,final_price,moneda}}
    r3 = requests.post(S3, json=master).json()   # -> {status, data:{id,in_stock,stock}}

    # 2) Dependientes
    r4 = requests.post(S4, json=r1["data"]).json()  # -> {data:{id,valid,token}}
    r5 = requests.post(S5, json=r2["data"]).json()  # -> {data:{id,ticket,amount,moneda}}

    # 3) Ensamble final
    final = {
        "id": master.get("id"),
        "valid": r4["data"]["valid"],
        "token": r4["data"]["token"],
        "final_price": r2["data"]["final_price"],
        "moneda": r2["data"]["moneda"],
        "in_stock": r3["data"]["in_stock"],
        "ticket": r5["data"]["ticket"],
        "stock": r3["data"]["stock"],
        "message": "Venta aprobada"
                   if (r4["data"]["valid"] and r3["data"]["in_stock"])
                   else "Venta pendiente o rechazada"
    }
    return jsonify(status="OK", result=final, steps={
        "s1_customer": r1,
        "s2_pricing": r2,
        "s3_inventory": r3,
        "s4_token": r4,
        "s5_ticket": r5
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
