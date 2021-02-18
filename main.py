# -*- coding: utf-8 -*-

import requests, os.path, time
# from git import Repo


head = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Easy-Kexts</title>
    <link href="https://cdn.bootcdn.net/ajax/libs/bulma/0.9.1/css/bulma.min.css" rel="stylesheet">
    <link href="https://cdn.bootcdn.net/ajax/libs/font-awesome/5.15.2/css/all.min.css" rel="stylesheet">
    <style>*{font-family: Helvetica, Tahoma, Arial, "PingFang SC", "Hiragino Sans GB", "Heiti SC","Microsoft YaHei", "WenQuanYiMicro Hei", sans-serif}</style>
    <script>
    document.addEventListener('DOMContentLoaded', () => {
        (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
            $notification = $delete.parentNode;
            $delete.addEventListener('click', () => {
            $notification.parentNode.removeChild($notification);
            });
        });
        });
    </script>
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
      <a href="https://dortania.github.io/OpenCore-Install-Guide/" target="_blank">
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
        <span>主页</span>
      </a>
    </li>
  </ul>
</nav>
<div class="container has-text-centered">
    <div class="notification is-success is-light">
      <button class="delete"></button>
      本次更新时间
"""
headplus = """
    </div>
</div>
<section class="section" name="Core">
    <div class="container">
        <div class="columns is-vcentered is-centered">
            <table class="table is-bordered is-striped is-hoverable">
                <thead>
                <tr>
                    <th><abbr>一级分类</abbr></th>
                    <th><abbr>二级分类</abbr></th>
                    <th><abbr>项目名称</abbr></th>
                    <th><abbr>版本标签</abbr></th>
                    <th><abbr>发布时间</abbr></th>
                    <th><abbr>下载地址</abbr></th>
                </tr>
                </thead>
                <tfoot>
"""
head = head + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + headplus
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


def get_file( sort1, sort2, owner_repo):
    # GET /repos/:owner/:repo/releases/ api参考 https://developer.github.com/v3/repos/releases/
    url = "https://api.github.com/repos/" + owner_repo + "/releases"

    # 转换成JSON
    json = requests.get(url).json()

    # 获取Filename 下载多个文件并准备HTML
    downloadlink = "<th>"
    assets = len(json[0]["assets"])
    while assets >= 1:
        assets = assets - 1
        filename = json[0]["assets"][assets]['name']
        if os.path.isfile(filename):
            print("File exists File name is   " + filename)
        else:
            file = requests.get(json[0]["assets"][assets]['browser_download_url'])
            with open(filename, "wb") as code:
                code.write(file.content)
            print("Download Finished File Name is   " + filename)
        downloadlink = downloadlink + '<a href="https://f002.backblazeb2.com/file/kexts-by-pcbeta-everyve/' + filename + '"target="_blank"><span class="tag is-link">' + filename + '</span></a>'
    return str(align + ('<tr><th><span class="tag is-primary is-light">'+sort1 + '</span></th>') + newline + align\
               + ('<th><span class="tag is-primary is-light">'+sort2 + '</span></th>') + newline + align\
               + ('<th><a href="https://github.com/'+owner_repo+'" target="_blank"><span class="tag is-primary">' + owner_repo +'</span></a></th>') + newline + align\
               + ('<th><span class="tag is-success is-light">'+ json[0]["tag_name"]+'</span></th>') + newline + align\
               + ('<th><span class="tag is-success">'+json[0]["published_at"]+'</span></th>') + newline + align + downloadlink + "</th>" + (newline + align) + "</tr>")


jsonx = requests.get("https://raw.githubusercontent.com/woq/Hackintosh-Resources/master/testx.json").json()
x = len(jsonx["list"])
y = 0
while y < x:
    head = head + get_file(jsonx["list"][y]["sort1"], jsonx["list"][y]["sort2"], jsonx["list"][y]["repo"])
    time.sleep(3)
    y = y + 1

with open("index.html", "w") as f:
    f.write(head+foot)


'''
dirfile = os.path.abspath('')
repo = Repo(dirfile)


g = repo.git
g.add("--all")
g.commit("-m auto update")
g.push()
print("Successful push!")
'''