heroku-bottle
===

To practice deploying bottle app on heroku.

## Required tools

### git

Install it.

### heroku cli

Install from [here](https://devcenter.heroku.com/articles/heroku-cli).

### pipenv

```bash
pip install pipenv
pipenv install --python 3.7
pipenv shell
```

```bash
pipenv install bottle
pip freeze > requirements.txt
echo web: python app.py > Procfile
```

## Installation

```bash
pipenv install
```

## How to upload to Heroku

```bash
git push --force-with-lease heroku dev:master
```

## Open

```bash
python app.py
```

Open localhost:5000
