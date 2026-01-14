# Pre Reqs
# Require psutil installed 
# install using python -m pip install psutil

# Import Tools
import datetime
import psutil
import time

def show_system_info():
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    boot_time = psutil.boot_time()
    uptime_seconds = int(time.time() - boot_time)

    days = uptime_seconds // 86400
    hours = (uptime_seconds % 86400) // 3600
    minutes = (uptime_seconds % 3600) // 60

# Show / Print findings (Static)
    print(f"CPU usage: {cpu}%")
    print(f"Memory usage: {memory.percent}%")
    print(f"Memory used: {memory.used // (1024**3):.2f} GB")
    print(f"Disk usage: {disk.used // (1024**3):.2f} GB")
    print(f"Computer uptime: {days}d {hours}h {minutes}m")

    log_event("INFO", f"CPU usage: {cpu}%")
    log_event("INFO", f"Memory usage: {memory.percent}%")
    log_event("INFO", f"Disk usage: {disk.percent}%")
    log_event("INFO", f"Uptime: {days}d {hours}h {minutes}m")

# (Observe) - Agentic 1A
def collect_system_info():
    boot_time = psutil.boot_time()
    uptime_seconds = int(time.time() - boot_time)

    return {
        "cpu": psutil.cpu_percent(interval=0.5),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "uptime_days": uptime_seconds // 86400
    }

# Define variables for Top 5 CPU Processes (Apps)
def top_cpu_processes(limit=5):
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes.sort(key=lambda p: p['cpu_percent'], reverse=True)
    return processes[:limit]

# Define variables for Top 5 Memory Processes (Apps)
def top_memory_processes(limit=5):
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes.sort(key=lambda p: p['memory_percent'], reverse=True)
    return processes[:limit]

# Define variables for Top 5 DISK I/O Processes (Apps)
def top_disk_processes(limit=5):
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'io_counters']):
        try:
            io = proc.info['io_counters']
            if io:
                processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'read_bytes': io.read_bytes,
                    'write_bytes': io.write_bytes
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes.sort(key=lambda p: p['read_bytes'] + p['write_bytes'], reverse=True)
    return processes[:limit]


def evaluate_system(stats):
    if stats["cpu"] > 80:
        log_event("WARNING", f"High CPU usage: {stats['cpu']}%")
        for proc in top_cpu_processes():
            log_event(
                "INFO",
                f"CPU Proc: {proc['name']} (PID {proc['pid']}) - {proc['cpu_percent']}%"
            )

    if stats["memory"] > 80:
        log_event("WARNING", f"High memory usage: {stats['memory']}%")
        for proc in top_memory_processes():
            log_event(
                "INFO",
                f"MEM Proc: {proc['name']} (PID {proc['pid']}) - {proc['memory_percent']:.2f}%"
            )

    if stats["disk"] > 90:
        log_event("WARNING", f"High disk usage: {stats['disk']}%")
        for proc in top_disk_processes():
            total_io = proc['read_bytes'] + proc['write_bytes']
            log_event(
                "INFO",
                f"DISK Proc: {proc['name']} (PID {proc['pid']}) - {total_io / (1024**2):.2f} MB"
            )

    if stats["uptime_days"] > 30:
        log_event("INFO", "System uptime exceeds 30 days")

def log_event(level, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp} [{level}] {message}\n"

# Print to screen
    print(log_line.strip())

# Write to log file
    with open("agent.log", "a") as log_file:
        log_file.write(log_line)

def main():
    today = datetime.date.today()
    name = input("Enter your name: ")
    print(f"Hello, {name}! Today is {today}. Welcome to your Python agent.")
    show_system_info()
    log_event("INFO", "Agent started")

    while True:
        stats = collect_system_info()
        evaluate_system(stats)

        time.sleep(30)  # wait 30 seconds before next check

if __name__ == "__main__":
    main()





