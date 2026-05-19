# Raspberry Pi Monitoring Stack

A containerised Raspberry Pi monitoring and observability stack running on a Raspberry Pi using Docker Compose, Prometheus, Grafana, Alertmanager and Pi-hole DNS filtering.

---

## Features

### Core Monitoring
- Real-time Raspberry Pi system monitoring
- Custom Prometheus metrics using Flask and psutil
- Dockerised monitoring services
- Docker Compose orchestration
- Nginx reverse proxy

### Observability Stack
- Prometheus metrics scraping
- Grafana operational dashboards
- Alertmanager alert routing
- Slack webhook alert notifications
- Custom Prometheus alert rules

### Pi-hole DNS Monitoring
- Pi-hole DNS filtering and telemetry
- Pi-hole Prometheus exporter
- DNS query monitoring
- Blocked query analytics
- Client activity monitoring
- Upstream DNS visibility

### Operational Features
- Health check endpoint
- Persistent Grafana storage
- Environment variable configuration
- Containerised architecture
- Real-time dashboard monitoring
- Infrastructure observability testing

---

## Metrics Collected

### Raspberry Pi Metrics
- CPU usage
- Memory usage
- Disk usage
- Raspberry Pi temperature

### Pi-hole Metrics
- Total DNS queries
- Blocked DNS queries
- Active clients
- Query status breakdown
- Query type analysis
- Upstream DNS destinations
- DNS traffic trends
- Blocklist statistics

---

## Technology Stack

- Python
- Flask
- Docker
- Docker Compose
- Nginx
- Prometheus
- Grafana
- Alertmanager
- Pi-hole
- psutil

---

## Architecture

![Pi-hole Observability Architecture](docs/images/pihole-observability-architecture.png)

This architecture demonstrates a containerised Pi-hole observability stack running on a Raspberry Pi using Docker Compose. Prometheus scrapes DNS metrics from the Pi-hole exporter, Grafana visualises operational dashboards and Alertmanager routes alerts to Slack via webhook notifications.

---

## Monitoring & Alerting

### Prometheus Alerts
- High CPU usage
- High disk usage
- High Raspberry Pi temperature
- Pi-hole exporter down
- No active Pi-hole clients
- High blocked DNS query percentage

### Alert Routing
- Prometheus evaluates alert rules
- Alertmanager routes notifications
- Slack webhook notifications for incidents

---

## Pi-hole Dashboards

### Dashboard 1 — Pi-hole Operations Overview
- Pi-hole availability
- DNS request volume
- Blocked DNS queries
- Active clients
- DNS traffic trends
- Query resolution efficiency

### Dashboard 2 — Pi-hole Analytics & Troubleshooting
- Query type analysis
- DNS reply analysis
- Upstream DNS destinations
- Client activity monitoring
- DNS query trends
- Resolver behaviour analysis

---

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

---

## Service Access

- Pi-hole Admin UI: `http://<pi-ip>:8081`
- Prometheus: `http://<pi-ip>:9090`
- Grafana: `http://<pi-ip>:3000`
- Alertmanager: `http://<pi-ip>:9093`

---

## Health Check

```bash
curl http://localhost/health
```

---

## Metrics Endpoint

```bash
curl http://localhost/metrics
```

---

## Operational Testing

The project includes:

- Live DNS traffic monitoring
- Pi-hole client testing
- Alert validation testing
- Slack notification testing
- Dashboard observability validation
- Controlled staged rollout testing

---

## Future Changes

- HTTPS/TLS support
- Centralised logging
- Grafana provisioning
- DNS-over-HTTPS
- Authentication and access control
- Cloud deployment
- CI/CD pipeline
- Uptime monitoring
