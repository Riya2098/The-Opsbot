import openai

#openai.api_key = "sk-..."  # or use env var
openai.api_key = os.getenv("OPENAI_API_KEY")

with open("incident_logs.txt", "r") as f:
    logs = f.read()

prompt = f"""
You are an AI DevOps assistant. Given the following logs, identify the possible causes of high CPU usage and suggest remediation steps.

Logs:
{logs}
"""

response = openai.ChatCompletion.create(
    model="gpt-4",  # or "gpt-3.5-turbo"
    messages=[{"role": "user", "content": prompt}]
)

result = response.choices[0].message.content
print("📊 LLM Analysis:\n", result)

# Save output for notification
with open("rca.txt", "w") as f:
    f.write(result)
