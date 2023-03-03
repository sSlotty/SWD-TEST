import requests
import json

url = "http://127.0.0.1:8000/api/send/"

payload = json.dumps({
  "subject": "Test subject from API",
  "message": "Test message from API",
  "name": "Thanathip",
  "to": "thanathipch9@gmail.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)