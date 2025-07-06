from flask import Flask, request
import subprocess
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    print("🚨 Received Alert:", data)

    # Calculate time window (last 2 minutes)
    now = datetime.utcnow()
    since = (now - timedelta(minutes=2)).strftime('%H:%M:%S')

    try:
        # Extract logs from /var/log/syslog
        logs = subprocess.check_output(f"awk '$3 >= \"{since}\"' /var/log/syslog", shell=True).decode()
    except subprocess.CalledProcessError as e:
        logs = f"Error retrieving logs: {e}"

    # Save logs for analysis
    with open("incident_logs.txt", "w") as f:
        f.write(logs)

    print("✅ Logs saved to incident_logs.txt")

    # Trigger LLM-based log analysis
    try:
        subprocess.run(["python3", "analyze.py"], check=True)
        print("🧠 analyze.py executed.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running analyze.py: {e}")

    return '', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
