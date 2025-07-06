import subprocess
import time
from prometheus_api_client import PrometheusConnect

prom = PrometheusConnect(url="http://localhost:9090", disable_ssl=True)

def get_cpu():
    query = '100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)'
    result = prom.custom_query(query)
    return float(result[0]['value'][1]) if result else 0.0

while True:
    cpu = get_cpu()
    print(f"🔥 CPU Usage: {cpu:.2f}%")
    if cpu > 80:
        print("⚠️ High CPU detected, triggering analysis + remediation...")
        subprocess.run(["python3", "analyze.py"])
        subprocess.run(["python3", "remediate.py"])
        subprocess.run(["python3", "notify.py"])
    time.sleep(60)
