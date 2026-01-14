# Python System Monitoring Agent

A lightweight Python system monitoring agent that collects and evaluates
CPU, memory, disk usage, and system uptime using `psutil`.

The agent logs system health events, identifies top resource-consuming
processes, and continuously monitors system performance.

---

## Features

- CPU, memory, and disk usage monitoring
- System uptime tracking
- Top CPU, memory, and disk I/O process detection
- Automatic logging with timestamps
- Continuous monitoring loop (30-second intervals)
- Ubuntu/Linux/WIndows compatible

---

## Requirements

- Python 3.8+
- psutil

---

## Installation

### Ubuntu

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/python-system-agent.git
cd python-system-agent
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
```

## Usage

Run the agent:
python agent.py

The agent will:

Prompt for your name
Display system statistics
Log events to agent.log
Monitor system health every 30 seconds
Stop execution with:
CTRL + C

# Example Output
CPU usage: 12.4%
Memory usage: 45%
Disk usage: 63%
Computer uptime: 2d 4h 10m
2026-01-14 10:42:01 [INFO] Agent started

## Future Improvements
Run as a systemd service
JSON / structured logging
Alerting (email)
Configurable thresholds
Cross-platform support (Windows/macOS)
