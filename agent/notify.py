import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

slack_token = os.getenv("SLACK_TOKEN")
channel = os.getenv("SLACK_CHANNEL", "#alerts")

client = WebClient(token=slack_token)

with open("rca.txt") as f:
    analysis = f.read()

message = f"""
*🚨 High CPU Alert*
*Root Cause Analysis:*\n{analysis}
*✅ Action Taken:* Auto-remediated (container/service restarted)
*🕒 Timestamp:* {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

try:
    client.chat_postMessage(channel=channel, text=message)
    print("📩 Slack notification sent.")
except SlackApiError as e:
    print(f"Slack error: {e.response['error']}")
