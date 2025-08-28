# s4_token/app.py
from flask import Flask, request, jsonify
import os, time, json

app = Flask(__name__)
TOKENS_DIR = "/data/tokens"
os.makedirs(TOKENS_DIR, exist_ok=True)

@app.get("/health")
def health():
    return jsonify(status="OK"), 200

@app.post("/process")
def process():
    data = request.get_json(force=True)
    valid = bool(data.get("valid"))
    token = f"TOKEN-{data.get('id')}-{int(time.time())%100000}" if valid else None
    result = {"id": data.get("id"), "valid": valid, "token": token}

    # Guardar en volumen
    if token:
        file_path = os.path.join(TOKENS_DIR, f"token-{data.get('id')}.json")
        with open(file_path, "w") as f:
            json.dump(result, f, indent=2)

    return jsonify(status="OK", data=result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
