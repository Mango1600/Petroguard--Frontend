import requests

url = "https://njrrjkcklaydsnqkfxud.supabase.co/auth/v1/token?grant_type=password"

anon_key = "PUT_YOUR_ANON_KEY_HERE"

headers = {
    "apikey": anon_key,
    "Content-Type": "application/json"
}

data = {
    "email": "mariam@sahwaadpet.com",
    "password": "Pilot@12345"
}

try:
    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=15
    )

    print("STATUS:", response.status_code)
    print("RESPONSE:")
    print(response.text)

except Exception as e:
    print("ERROR:")
    print(e)
