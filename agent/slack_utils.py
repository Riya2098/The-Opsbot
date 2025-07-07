import os
import datetime
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()

client = WebClient(token=os.getenv("SLACK_TOKEN"))

with open("rca.txt") as f:
    analysis = f.read()

message = f"""
*High CPU Alert*
Root Cause: {analysis}
Action: Auto-restarted container
Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

response = client.chat_postMessage(
    channel=os.getenv("SLACK_CHANNEL_ID"),
    text=message
)

print(response)
