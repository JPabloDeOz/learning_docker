# s8_reader/app.py
from flask import Flask, jsonify
import os, json

app = Flask(__name__)
TOKENS_DIR = "/data/tokens"  # apunta al mismo volumen que S4

@app.get("/health")
def health():
    return jsonify(status="OK"), 200

@app.get("/read_tokens/<id>")
def read_token(id):
    fname = f"token-{id}.json"
    path = os.path.join(TOKENS_DIR, fname)
    if not os.path.exists(path):
        return jsonify(status="ERROR", message="Archivo no encontrado"), 404
    with open(path) as f:
        content = json.load(f)
    return jsonify(status="OK", content=content), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
