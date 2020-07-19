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
                    <th><abbr>项目类型</abbr></th>
                    <th><abbr>项目名称</abbr></th>
                    <th><abbr>提交编译时间</abbr></th>
                    <th><abbr>编译完成时间</abbr></th>
                    <!--<th><abbr>更新说明</abbr></th>--> 
                    <th><abbr>下载地址</abbr></th>
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
newline = "\n"
align = "                "

def get_file(owner_repo,sort="自动编译"):
    # GET /repos/:owner/:repo/releases/ api参考 https://developer.github.com/v3/repos/releases/
    url = "https://api.github.com/repos/" + owner_repo + "/releases"
    # 转换成JSON
    json = requests.get(url).json()
    # 获取Filename 下载多个文件并准备HTML
    downloadlink = "<th>"
    assets = len(json[0]["assets"])
    if assets > 1:
        while assets >= 1:
            assets = assets - 1
            filename = json[0]["assets"][assets]['name']
            file = requests.get(json[0]["assets"][assets]['browser_download_url'])
            with open(filename, "wb") as code:
                code.write(file.content)
            print("Download Finished File Name is   " + filename)
            downloadlink = downloadlink + '<a href="https://gitee.com/evu/Easy-Kexts/raw/master/' + filename + '"target="_blank"><span class="tag is-link">' + filename + '</span></a>'

    return str(align + ('<tr><th><span class="tag is-primary is-light">'+sort + '</span></th>') + newline + align\
               + ('<th><a href="https://github.com/'+owner_repo+'" target="_blank"><span class="tag is-primary">' + owner_repo +'</span></a></th>') + newline + align\
               + ('<th><span class="tag is-info">'+ json[0]["tag_name"]+'</span></th>') + newline + align\
               + ('<th><span class="tag is-success">'+json[0]["published_at"]+'</span></th>') + newline + align + downloadlink + "</th>" + (newline + align) + "</tr>")


head = head + get_file("woq/Lilu")
head = head + get_file("woq/AppleALC")
head = head + get_file("woq/VirtualSMC")
head = head + get_file("woq/OpenCorePkg")
head = head + get_file("woq/VoodooInput")
head = head + get_file("woq/AirportBrcmFixup")



with open("index.html", "w") as f:
    f.write(head+foot)

# 自动部署

dirfile = os.path.abspath('')
repo = Repo(dirfile)


g = repo.git
g.add("--all")
g.commit("-m auto update")
g.push()
print("Successful push!")