# backend/utils/monitor.py
import psutil
import time
from typing import Dict

def sample_metrics() -> Dict:
    """Single-sample snapshot of system metrics."""
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()._asdict()
    disk = psutil.disk_usage('/')._asdict()
    net = psutil.net_io_counters()._asdict()
    processes = []
    for p in psutil.process_iter(['pid','name','cpu_percent','memory_percent']):
        try:
            info = p.info
            processes.append(info)
        except Exception:
            continue
    return {
        'timestamp': int(time.time()),
        'cpu_percent': cpu,
        'memory': mem,
        'disk': disk,
        'network': net,
        'processes': processes[:20]
    }
