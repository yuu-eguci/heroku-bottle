heroku-bottle
===

To practice deploying bottle app on heroku.

## Installation

### git

Install it.

### heroku cli

Install from [here](https://devcenter.heroku.com/articles/heroku-cli).

### pipenv

```bash
pip install pipenv
pipenv install --python 3.7
```

### Others

```bash
pipenv install bottle
pip freeze > requirements.txt
echo web: python app.py > Procfile
```
