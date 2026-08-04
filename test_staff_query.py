import requests
from pathlib import Path

env = {}

for line in Path(".env").read_text().splitlines():
    if "=" in line:
        k, v = line.split("=", 1)
        env[k] = v

url = env["VITE_SUPABASE_URL"] + "/rest/v1/staff?select=*&user_id=eq.USER_ID_HERE"

headers = {
    "apikey": env["VITE_SUPABASE_ANON_KEY"],
    "Authorization": "Bearer " + env["VITE_SUPABASE_ANON_KEY"]
}

r = requests.get(
    url,
    headers=headers,
    timeout=15
)

print("STATUS:", r.status_code)
print(r.text[:500])
