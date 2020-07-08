import requests
import os

exp = "https://github.com/acidanthera/Lilu/releases/download/1.4.4/Lilu-1.4.4-RELEASE.zip"



def get_file(repo):
    url = "https://api.github.com/repos/" + repo + "/releases/latest"
    githuburl = "https://github.com/"
    downloadpath = "/releases/download/"
    fanxiegang = "/"
    version = requests.get(url).json()["tag_name"]
    if repo == "acidanthera/Lilu":
        filename = "Lilu-" + version + "-RELEASE.zip"
        if os.path.isfile("./Lilu/" + filename):
            print("Lilu is ok!!! The Version = " + version)
        else:
            file = requests.get(githuburl + repo + version + fanxiegang + filename)
            with open("./Lilu/"+filename, "wb") as code:
                code.write(file.content)
    if repo == "acidanthera/OpenCorePkg":
        filename = "OpenCore-" + version + "-RELEASE.zip"
        if os.path.isfile("./OpenCore/" + filename):
            print("OpenCore is ok!!! The Version = " + version)
        else:
            file = requests.get(githuburl + repo + version + fanxiegang + filename)
            with open("./OpenCore/" + filename, "wb") as code:
                code.write(file.content)


get_file("acidanthera/Lilu")
get_file("acidanthera/OpenCorePkg")