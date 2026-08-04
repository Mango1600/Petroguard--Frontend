import requests
from pathlib import Path

env = {}

for line in Path(".env").read_text().splitlines():
    if "=" in line:
        k, v = line.split("=", 1)
        env[k] = v

url = env["VITE_SUPABASE_URL"] + "/auth/v1/token?grant_type=password"

headers = {
    "apikey": env["VITE_SUPABASE_ANON_KEY"],
    "Content-Type": "application/json"
}

data = {
    "email": "mariam@sahwaadpet.com",
    "password": "Pilot@12345"
}

r = requests.post(
    url,
    headers=headers,
    json=data,
    timeout=15
)

print("STATUS:", r.status_code)
print(r.text[:300])
