from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="OK"), 200

@app.post("/process")
def process():
    data = request.get_json(force=True)  # espera {id, valid, nombre}
    valid = bool(data.get("valid"))
    token = f"TOKEN-{data.get('id')}-{int(time.time())%100000}" if valid else None
    result = {
        "id": data.get("id"),
        "valid": valid,
        "token": token
    }
    return jsonify(status="OK", data=result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
