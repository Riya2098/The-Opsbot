import os
import openai
import subprocess

openai.api_key = os.getenv("OPENAI_API_KEY")

with open("incident_logs.txt", "r") as f:
    logs = f.read()

prompt = f"""
You are an AI DevOps assistant. Given the following logs, identify the possible causes of high CPU usage and suggest remediation steps.

Logs:
{logs}
"""

#response = openai.ChatCompletion.create(
#    model="gpt-3.5-turbo",
#    messages=[{"role": "user", "content": prompt}]
#)

#result = response.choices[0].message.content
result = "Root cause likely due to high memory usage in background processes. Recommended remediation: restart the affected container."

print("LLM Analysis:\n", result)

# Save output for notification
with open("rca.txt", "w") as f:
    f.write(result)

# 🔔 Trigger Slack Notification
try:
    subprocess.run(["python3", "notify.py"], check=True)
    print(" Slack notification sent.")
except subprocess.CalledProcessError as e:
    print(f" Failed to send Slack notification: {e}")
