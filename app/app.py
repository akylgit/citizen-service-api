from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

services = [
    {
        "id": 1,
        "name": "Digital ID",
        "status": "available",
        "department": "Digital Services"
    },
    {
        "id": 2,
        "name": "Vehicle Registration",
        "status": "available",
        "department": "Transport Services"
    },
    {
        "id": 3,
        "name": "Property Registration",
        "status": "maintenance",
        "department": "Land Services"
    }
]


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/ready")
def ready():
    return jsonify({
        "status": "ready"
    })


@app.route("/api/v1/services")
def get_services():
    return jsonify({
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "services": services
    })


@app.route("/api/v1/services/<int:service_id>")
def get_service(service_id):
    for service in services:
        if service["id"] == service_id:
            return jsonify(service)

    return jsonify({
        "error": "Service not found"
    }), 404


@app.route("/")
def home():
    return jsonify({
        "application": "Citizen Service API",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "status": "running"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
