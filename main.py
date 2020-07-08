import requests
import os

exp = "https://github.com/acidanthera/Lilu/releases/download/1.4.4/Lilu-1.4.4-RELEASE.zip"



def get_file(repo):
    url = "https://api.github.com/repos/" + repo + "/releases/latest"

    version = requests.get(url).json()["tag_name"]
    if repo == "acidanthera/Lilu":
        filename = "Lilu-" + version + "-RELEASE.zip"
        if os.path.isfile("./Lilu/" + filename):
            print("Lilu is ok" + version)
            exit()
        file = requests.get("https://github.com/" + repo + "/releases/download/" + version +"/" + filename)
        with open("./Lilu/"+filename, "wb") as code:
            code.write(file.content)

get_file("acidanthera/Lilu")