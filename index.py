# -*- coding: utf-8 -*-
import json,time,os.path
from jinja2 import Environment, FileSystemLoader
from git import Repo

env = Environment(loader=FileSystemLoader('./'))
tpl = env.get_template('template.html')

anything = json.load()
# sort1;sort2;projectName;projectNamelink;versionTag;releaseDate;updateWay=release,manual,direct;fileName;


CST = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open('index.html', 'w', encoding='utf8') as output:
    render_content = tpl.render(time=CST, list=anything)
    output.write(render_content)



# GitPython
dirfile = os.path.abspath('')
repo = Repo(dirfile)
g = repo.git
g.add("--all")
g.commit("-m auto update")
g.push()
print("Successful push!")
