# Raspberry Pi System Monitor

A lightweight full-stack system monitoring dashboard built with Flask and Python, deployed on a Raspberry Pi as a persistent Linux service.

## Features

- Real-time CPU usage monitoring
- Memory usage tracking
- Disk usage monitoring
- REST API backend (`/stats`)
- Web dashboard frontend (HTML + JavaScript)
- Auto-start on boot using systemd
- Accessible over local network

## Tech Stack

- Python + Flask + psutil
- HTML / JavaScript
- systemd (Linux service manager)

## Architecture

Browser → Flask Backend → psutil system metrics → JSON API → Frontend dashboard

## Deployment

Runs as a systemd service on Raspberry Pi:

## Setup

```bash
sudo systemctl start pimonitor.service 
pip install -r requirements.txt
python app.py
```

---
