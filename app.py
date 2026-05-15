from flask import Flask, jsonify, render_template
import psutil
import os
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Gauge

cpu_usage_gauge = Gauge("pi_cpu_usage_percent", "CPU usage percent")
memory_usage_gauge = Gauge("pi_memory_usage_percent", "Memory usage percent")
disk_usage_gauge = Gauge("pi_disk_usage_percent", "Disk usage percent")
temperature_gauge = Gauge("pi_temperature_celsius", "Raspberry Pi temperature")

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
    cpu_usage_gauge.set(psutil.cpu_percent())
    memory_usage_gauge.set(psutil.virtual_memory().percent)
    disk_usage_gauge.set(psutil.disk_usage("/").percent)

    temps = psutil.sensors_temperatures()

    if "cpu_thermal" in temps:
        temperature_gauge.set(temps["cpu_thermal"][0].current)

    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(
	host="0.0.0.0",
	port=int(os.getenv("PORT",5000)))
