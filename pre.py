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
    <link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/font-awesome/5.14.0/css/all.min.css">
</head>
<body>
<nav class="breadcrumb is-centered" aria-label="breadcrumbs">
  <ul>
    <li>
      <a href="http://bbs.pcbeta.com/">
        <span class="icon is-medium">
          <i class="fas fa-apple-alt" aria-hidden="true"></i>
        </span>
        <span>远景</span>
      </a>
    </li>
    <li>
      <a href="http://bbs.pcbeta.com/forum.php?gid=86" target="_blank">
        <span class="icon is-medium">
          <i class="fas fa-book" aria-hidden="true"></i>
        </span>
        <span>文档</span>
      </a>
    </li>
    <li>
      <a href="https://gitee.com/" target="_blank">
        <span class="icon is-medium">
          <i class="fab fa-gratipay" aria-hidden="true"></i>
        </span>
        <span>码云</span>
      </a>
    </li>
    <li>
      <a href="https://evu.gitee.io/easy-kexts/" target="_blank">
        <span class="icon is-medium">
          <i class="fas fa-bolt" aria-hidden="true"></i>
        </span>
        <span>预览</span>
      </a>
    </li>
    <li>
      <a href="https://evu.gitee.io/easy-kexts-stable/" target="_blank">
        <span class="icon is-medium">
          <i class="fas fa-lightbulb" aria-hidden="true"></i>
        </span>
        <span>稳定</span>
      </a>
    </li>
  </ul>
</nav>
<section class="section" name="Core">
    <div class="container">
        <div class="columns is-vcentered is-centered is-striped is-hoverable">
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

def get_file(owner_repo,sort="预览"):
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
               + ('<th><span class="tag is-success is-light">' + json[0]["tag_name"]+'</span></th>') + newline + align\
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