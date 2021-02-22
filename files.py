# -*- coding: utf-8 -*-
import requests, os.path, json, time

# 下载完成后,重写版本信息,发布时间,文件名,以及文件链接
# 读取本地JSON
with open('new.json', 'r') as load_f:
    jsonData = json.load(load_f)

i = 0
for value in jsonData:
    # 校验更新方式
    if jsonData[i]['updateWay'] == 'release':
        # GET /repos/:owner/:repo/releases/ api参考 https://developer.github.com/v3/repos/releases/
        url = url = "https://api.github.com/repos/" + jsonData[i]['projectName'] + "/releases"
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
            jsonData[i]['files'] = '<a href="https://cdn.jsdelivr.net/gh/woq/Hackintosh-Resources/' + filename \
                                   + '"target="_blank"><span class="tag is-link">' + filename + '</span></a>'
            jsonData[i]['projectLink'] = api[0]['url']
            jsonData[i]['versionTag'] = api[0]['tag_name']
            jsonData[i]['releaseDate'] = api[0]['published_at']
        time.sleep(3)
    i += 1

with open('new.json','w',encoding='utf8') as jsonDone:
    wtf = json.dumps(jsonData)
    jsonDone.write(wtf)
