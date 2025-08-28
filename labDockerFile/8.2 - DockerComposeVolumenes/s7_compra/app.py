# s7_compra/app.py
from flask import Flask, request, jsonify
import os, json, time

app = Flask(__name__)
TICKETS_DIR = "tickets"

os.makedirs(TICKETS_DIR, exist_ok=True)

@app.get("/health")
def health():
    return jsonify(status="OK"), 200

@app.post("/save")
def save():
    data = request.get_json(force=True)
    file_name = f"ticket-{data.get('id')}-{int(time.time())}.json"
    file_path = os.path.join(TICKETS_DIR, file_name)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
    return jsonify(status="OK", message="Ticket guardado", file=file_name), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
