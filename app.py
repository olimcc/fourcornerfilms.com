from bottle import route, run, template, static_file
import logging

logging.basicConfig(filename='log.txt', format=logging.BASIC_FORMAT)

@route('/static/<path:path>')
def server_static(path):
    return static_file(path, root='./static/')

@route('/projects/<path:path>')
def server_project(path):
    if not path.endswith('.html'):
        path = path + '/index.html'
    return static_file(path, root='./projects/')

@route('/')
def index():
    return static_file('index.html', root='./')

run(host='localhost', port=8000)


