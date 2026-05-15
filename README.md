# Raspberry Pi Monitoring Stack

A containerised Raspberry Pi monitoring and observability stack built with Flask, Docker, Nginx, Prometheus and Grafana.

## Features

- Real-time Raspberry Pi system monitoring
- Dockerised Flask application
- Docker Compose orchestration
- Nginx reverse proxy
- Prometheus metrics scraping
- Grafana dashboards
- Custom Raspberry Pi metrics
- Persistent Grafana storage
- Health check endpoint
- Environment variable configuration

## Metrics Collected

- CPU usage
- Memory usage
- Disk usage
- Raspberry Pi temperature

## Technology Stack

- Python
- Flask
- Docker
- Docker Compose
- Nginx
- Prometheus
- Grafana
- psutil

## Architecture

```text
Browser
   ↓
Nginx Reverse Proxy
   ↓
Flask PiMonitor Application
   ↓
Prometheus Metrics Endpoint
   ↓
Grafana Dashboards
```

Docker Compose orchestrates all services and networking.

## Project Structure

```text
.
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── nginx/
│   └── default.conf
├── prometheus/
│   └── prometheus.yml
├── templates/
└── README.md
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Am1tp/raspberry-pi-system-monitor.git
cd raspberry-pi-system-monitor
```

### Start the Stack

```bash
docker compose up -d --build
```

## Service Access

- Flask Dashboard: `http://<pi-ip>/`
- Prometheus: `http://<pi-ip>:9090`
- Grafana: `http://<pi-ip>:3000`

## Health Check

```bash
curl http://localhost/health
```

## Custom Metrics Endpoint

```bash
curl http://localhost/metrics
```

## Future ideas/improvements

- Alerting
- Cloud deployment
- HTTPS support
- Centralised logging
- CI/CD pipeline
- Authentication
