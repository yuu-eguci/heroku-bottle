
import os
from bottle import route, run, view, static_file

@route('/')
def hello_world():
    return 'Hello World!'

@route('/tpl')
@view('tpl')
def tpl():
    return {
        'aaaa': 'aaaa',
        'bbbb': 'bbbb',
    }

@route('/img')
def img():
    return '<img src="/static/python-logo.png" />'

@route('/static/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./static')

# Run with different setting on Heroku from on local.
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        )
else:
    run(host='0.0.0.0',
        port=8080,
        reloader=True,  # Enable auto reload.
        debug=True,     # Display error detail on browser.
        )
