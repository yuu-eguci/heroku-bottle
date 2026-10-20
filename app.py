from pathlib import Path

from bottle import TEMPLATE_PATH, Bottle, static_file, view

BASE_DIR = Path(__file__).resolve().parent
STATIC_ROOT = str(BASE_DIR / "static")

# Resolve templates relative to this file, not the current working directory.
TEMPLATE_PATH.insert(0, str(BASE_DIR / "views"))

app = Bottle()


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/tpl")
@view("tpl")
def tpl():
    return {
        "aaaa": "aaaa",
        "bbbb": "bbbb",
    }


@app.route("/img")
def img():
    return '<img src="/static/python-logo.png" />'


@app.route("/static/<file_path:path>")
def static(file_path):
    return static_file(file_path, root=STATIC_ROOT)


if __name__ == "__main__":
    # Development server only; Docker and Heroku run gunicorn (see Dockerfile / Procfile).
    app.run(
        host="127.0.0.1",
        port=8080,
        reloader=True,  # Enable auto reload.
        debug=True,  # Display error detail on browser.
    )
