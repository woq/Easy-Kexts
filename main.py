import requests
print(requests.get("https://github.com/acidanthera/Lilu/releases/latest").json())
