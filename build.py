import jinja2
import json
import os

BUILD_DIR = './'

def chunk(l, c):
    pos = 0
    while (pos<len(l)):
        yield l[pos: pos+c]
        pos = pos+c

# index
template = open('templates/index.html', 'r').read()
template = jinja2.Template(template)
configuration = json.loads(open('configs/index.json', 'r').read())
project_configs = [json.loads(open('configs/projects/'+c['config'], 'r').read()) for c in  configuration['projects']]
grouped_project_configs = chunk(project_configs, 2)

html = template.render(grouped_project_configs=grouped_project_configs)
fpath = os.path.join(BUILD_DIR, 'index.html')
with open(fpath, 'w') as outfile:
    outfile.write(html)

# projects
template = open('templates/project.html', 'r').read()
template = jinja2.Template(template)

for content in project_configs:
    html = template.render(**content)
    dirpath = os.path.join('build', 'projects', content['slug'])
    try:
        os.makedirs(dirpath)
    except OSError:
        pass
    fpath = os.path.join(dirpath, 'index.html')

    with open(fpath, 'w') as outfile:
        outfile.write(html)
