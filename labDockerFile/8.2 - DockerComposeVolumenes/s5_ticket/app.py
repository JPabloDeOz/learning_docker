from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="OK"), 200

@app.post("/process")
def process():
    data = request.get_json(force=True)  # espera {id, final_price, moneda}
    id_ = data.get("id")
    final_price = data.get("final_price")
    ticket = f"TICKET-{id_}-{str(final_price).replace('.', '')}"
    result = {
        "id": id_,
        "ticket": ticket,
        "amount": final_price,
        "moneda": data.get("moneda", "USD")
    }
    return jsonify(status="OK", data=result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
