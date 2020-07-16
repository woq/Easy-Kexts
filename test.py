import requests

json = requests.get("https://api.github.com/repos/williambj1/OpenCore-Factory/releases").json()
print(json[0]["url"])
