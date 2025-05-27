import requests

access_token = 'O6ifn1uNd1vnt/3q23gGtFjpwUI/FC2yOY4ypGOGCfzlQoOIORMB/YUHWa44wX/BVaqsYAjJBtn5s92hQ5CXOUmojuCpEcA14NQ1ppjFhGL6mInfx/sOfMQZHqpV7uhrZ7nYkiRDWLtgWtUPaBy7+AdB04t89/1O/w1cDnyilFU='
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
