import requests
import json

# ---------------------------
# Configuration
# ---------------------------
DEPLOYMENT_ID = "694138f65819ea20051624b5"
API_KEY = "Njk0MTNhYjdlZTliN2Y1NGUzOTZlZDdmOlJ4NHg4cWYvWnB4dEpFYTcwZGVMQnR0Nlo2bmhRQ1hvZ0ZHT3dIWXVEQ1E9"   # rotate if exposed earlier

URL = f"https://app.datarobot.com/api/v2/deployments/{DEPLOYMENT_ID}/predictions"

headers = {
    "Authorization": f"Token {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# ---------------------------
# Payload (RAW ARRAY for API v2)
# ---------------------------
payload = [
    {
        "gender": "Male",
        "age": 32,
        "tenure": 6,
        "monthly_charges": 100,
        "total_charges": 600,
        "contract_type": "Month-to-month",
        "internet_service": "Fiber optic",
        "payment_method": "Electronic check"
    }
]

# ---------------------------
# Make request
# ---------------------------
response = requests.post(
    URL,
    headers=headers,
    data=json.dumps(payload)
)

# ---------------------------
# Handle response
# ---------------------------
print("Status Code:", response.status_code)
print("Response JSON:")
print(json.dumps(response.json(), indent=2))

