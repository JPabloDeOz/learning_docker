from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="OK"), 200

@app.post("/process")
def process():
    data = request.get_json(force=True)
    precio = float(data.get("precio", 0))
    descuento = float(data.get("descuento", 0))
    final_price = round(precio * (1 - descuento/100.0), 2)
    result = {
        "id": data.get("id"),
        "final_price": final_price,
        "moneda": data.get("moneda", "USD")
    }
    return jsonify(status="OK", data=result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
