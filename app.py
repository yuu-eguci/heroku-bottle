
import os
from bottle import route, run, view

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
