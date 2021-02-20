# -*- coding: utf-8 -*-
import requests, os.path, time
from git import Repo



def githubrepo( sort1, sort2, owner_repo):
    # GET /repos/:owner/:repo/releases/ api参考 https://developer.github.com/v3/repos/releases/
    url = "https://api.github.com/repos/" + owner_repo + "/releases"
    api = requests.get(url).json()

    # 获取Filename 下载多个文件并准备HTML
    assets = len(api[0]["assets"])
    while assets >= 1:
        assets = assets - 1
        filename = api[0]["assets"][assets]['name']
        if os.path.isfile(filename):
            print("File exists File name is    " + filename)
        else:
            file = requests.get(api[0]["assets"][assets]['browser_download_url'])
            with open(filename, "wb") as code:
                code.write(file.content)
            print("Download Finished File Name is    " + filename)
        downloading = downloading + '<a href="https://cdn.jsdelivr.net/gh/woq/Hackintosh-Resources/' + filename + '"target="_blank"><span class="tag is-link">' + filename + '</span></a>'



# 下载Github项目里最新的一个tag的所有附件 备注 如果附件数量为0 会出致命错误
githubRepos = requests.get("https://raw.githubusercontent.com/woq/Easy-Kexts/master/main.json").json()
x = len(githubRepos["list"])
y = 0
while y < x:
    head = head + githubrepo(githubRepos["list"][y]["sort1"], githubRepos["list"][y]["sort2"], githubRepos["list"][y]["repo"])
    time.sleep(3)
    y = y + 1


import time, requests
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('D:\Code\Easy-Kexts'))

tpl = env.get_template('template.html')

anything = requests.get('https://github.com/woq/Easy-Kexts/raw/master/test3.json').json()
# sort1;sort2;projectName;projectNamelink;versionTag;releaseDate;updateWay=release,manual,direct;fileName;


CST = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open('index.html', 'w', encoding='utf8') as output:
    render_content = tpl.render(time=CST, list=anything)
    output.write(render_content)



head = head+manual('Ethernet','Realtek','LucyRTL8125Ethernet','https://github.com/Mieze/LucyRTL8125Ethernet','1.0.0','unknow','手动 + CDN','https://cdn.jsdelivr.net/gh/woq/Hackintosh-Resources/LucyRTL8125Ethernet-V1.0.0.zip','LucyRTL8125Ethernet-V1.0.0.zip')
head = head+manual('Ethernet','Atheros','AtherosE2200Ethernet','https://github.com/Mieze/AtherosE2200Ethernet','2.3.3','unknow','手动 + CDN','https://cdn.jsdelivr.net/gh/woq/Hackintosh-Resources/AtherosE2200Ethernet-V2.3.3.zip','AtherosE2200Ethernet-V2.3.3.zip')
head = head+manual('CORE','EFI/OC/Drivers/','HfsPlus.efi','https://github.com/acidanthera/OcBinaryData/blob/master/Drivers/HfsPlus.efi','unknown','unknown','直连 + CDN','https://cdn.jsdelivr.net/gh/acidanthera/OcBinaryData/Drivers/HfsPlus.efi','HfsPlus.efi')


# GitPython
dirfile = os.path.abspath('')
repo = Repo(dirfile)
g = repo.git
g.add("--all")
g.commit("-m auto update")
g.push()
print("Successful push!")
