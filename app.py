from flask import Flask, jsonify, render_template
import psutil
import os
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stats")
def stats():
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage("/")._asdict()
    })

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(
	host="0.0.0.0",
	port=int(os.getenv("PORT",5000)))
