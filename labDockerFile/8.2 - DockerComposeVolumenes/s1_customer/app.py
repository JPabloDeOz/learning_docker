from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="OK"), 200

@app.post("/process")
def process():
    data = request.get_json(force=True)
    result = {
        "id": data.get("id"),
        "nombre": data.get("nombre"),
        "valid": bool(data.get("id")) and bool(data.get("nombre"))
    }
    return jsonify(status="OK", data=result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
