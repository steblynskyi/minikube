import requests
import json

def send_teams_notification(webhook_url, message):
    # Create the payload to send
    payload = {
        "text": message
    }

    # Send the request to Teams using the webhook
    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

# Replace with your Teams webhook URL
webhook_url = "https://your.webhook.office.com/here"
message = "Hey MSTEAMS!"

# Send the notification
send_teams_notification(webhook_url, message)