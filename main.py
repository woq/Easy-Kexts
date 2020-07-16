import requests
import os
import time


def get_file(repo):
    # GET /repos/:owner/:repo/releases/tags/:tag
    url = "https://api.github.com/repos/" + repo + "/releases/latest"
    # 转换成JSON
    json = requests.get(url).json()
    # 获取Filename
    filename = json["assets"][0]['name']
    # 判断文件是否存在，避免重复下载
    if os.path.isfile(filename):
        print("文件已存在" + repo + "     " + json["tag_name"])
    else:
        file = requests.get(json["assets"][0]['browser_download_url'])
        with open(filename, "wb") as code:
            code.write(file.content)

        print("下载完毕" + repo + "     " + json["tag_name"])
    time.sleep(30)  # 避免过度频繁引起nuke
    return json["tag_name"], filename


get_file("acidanthera/Lilu")
get_file("acidanthera/OpenCorePkg")
