# -*- coding: utf-8 -*-
import requests
import os
from git import Repo


head = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Easy-Kexts</title>
    <link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/bulma/0.9.0/css/bulma.min.css">
</head>
<body>
<section class="section" name="Core">
    <div class="container">
        <div class="columns is-vcentered is-centered">
            <table class="table is-bordered ">
                <thead>
                <tr>
                    <th><abbr>类别</abbr></th>
                    <th><abbr>项目名</abbr></th>
                    <th><abbr>版本号</abbr></th>
                    <th><abbr>更新时间</abbr></th>
                    <th><abbr>更新说明</abbr></th>
                    <th><abbr>下载连接</abbr></th>
                </tr>
                </thead>
                <tfoot>
"""

foot = """
                </tfoot>
            </table>
        </div>
    </div>
</section>
</body>
</html>
"""
suojin = "                "
bigsuojin = "                   "


def get_file(repo, sort):
    # GET /repos/:owner/:repo/releases/tags/:tag
    url = "https://api.github.com/repos/" + repo + "/releases/latest"
    # 转换成JSON
    json = requests.get(url).json()
    # 获取Filename
    filename = json["assets"][0]['name']
    # 判断文件是否存在，避免重复下载
    if os.path.isfile(filename):
        print("文件已存在" + repo + "\r" + json["tag_name"])
    else:
        file = requests.get(json["assets"][0]['browser_download_url'])
        with open(filename, "wb") as code:
            code.write(file.content)

        print("下载完毕" + repo + "\r" + json["tag_name"])

    return str((suojin + "<tr>") + ('<th><span class="tag is-primary is-light">'+sort +'</span></th>') + ('<th><a href="https://github.com/'+repo+'" target="_blank"><span class="tag is-primary">'+ repo+'</span></a></th>') +('<th><span class="tag is-info">'+ json["tag_name"]+'</span></th>')+('<th><span class="tag is-success">'+json["published_at"]+'</span></th>')+('<th><span class="tag is-warning is-light">'+json["html_url"] +'</span></th>')+('<th><a href="https://gitee.com/evu/Easy-Kexts/raw/master/'+ filename +'" target="_blank"><span class="tag is-link">下载</span></a></th>')+ ("\n" + suojin + "</tr>"))


head = head + get_file("acidanthera/Lilu", "CORE")
head = head + get_file("acidanthera/OpenCorePkg", "CORE")
head = head + get_file("acidanthera/VirtualSMC", "CORE")
head = head + get_file("acidanthera/AppleALC", "AUDIO")
head = head + get_file("acidanthera/WhateverGreen", "GPU")
head = head + get_file("acidanthera/VoodooPS2", "Trackpad")

with open("index.html", "w") as f:
    f.write(head+foot)

dirfile = os.path.abspath('') # code的文件位置，我默认将其存放在根目录下
repo = Repo(dirfile)

g = repo.git
g.add("--all")
g.commit("-m auto update")
g.push()
print("Successful push!")