import requests


def get_latest_version(owerandprojectname):
    url = "https://api.github.com/repos/" + owerandprojectname + "/releases/latest"
    return requests.get(url).json()["tag_name"]


print(get_latest_version("acidanthera/Lilu"))