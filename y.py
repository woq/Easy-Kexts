import jinja2,time
from jinja2 import  Environment,FileSystemLoader
env = Environment(loader=FileSystemLoader('D:\Code\Easy-Kexts'))

tpl = env.get_template('template.html')


# sort1;sort2;projectName;projectNamelink;versionTag;releaseDate;updateWay=release,manual,direct;fileName;
CST = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open('report.html', 'w', encoding='utf8') as fout:
    render_content = tpl.render(time=CST)
    fout.write(render_content)
