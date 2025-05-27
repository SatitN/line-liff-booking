import requests

access_token = ''
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

body = {
    "view": {
        "type": "full",
        "url": "https://your-username.github.io/queue-booking/"
    },
    "description": "LIFF Booking App",
    "features": {
        "ble": False,
        "qrCode": False
    },
    "permanentLinkPattern": "concat",
    "scope": ["profile", "chat_message.write"]
}

res = requests.post("https://api.line.me/liff/v1/apps", headers=headers, json=body)
print(res.status_code)
print(res.json())
