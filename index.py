# -*- coding: utf-8 -*-
import json,time,os.path
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('./'))
tpl = env.get_template('template.html')

with open('new.json', 'r') as load_f:
    jsonData = json.load(load_f)


CST = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open('index.html', 'w', encoding='utf8') as output:
    render_content = tpl.render(time=CST, list=jsonData)
    output.write(render_content)


# GitPython
"""
from git import Repo
dirfile = os.path.abspath('')
repo = Repo(dirfile)
g = repo.git
g.add("--all")
g.commit("-m auto update")
g.push()
print("Successful push!")
"""
