# python-system-agent
python-system-agent

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
