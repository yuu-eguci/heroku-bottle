heroku-bottle
===

Bottle アプリを Heroku へデプロイする練習用。

- Docker: 対応!
- Python: 3.14!
- Linter: Ruff!
- Test: pytest!
- Bottle 0.13

## パッと実行してみたい

```bash
docker compose up --build
# http://localhost:8080 を開くと Hello World! が出る
# http://localhost:8080/tpl はテンプレート、 /img は静的画像のページ
```

## 必要なもの

- Git
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) (Heroku へデプロイする場合)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) または Docker Engine + Compose v2 (Docker で動かす場合)

## ローカルで動かす

Docker を使わずローカルで動かす場合:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python app.py
```

`python app.py` は Bottle 付属の開発サーバを `http://127.0.0.1:8080` で起動する。
ソースを書き換えると自動リロードする。
エラーの詳細もブラウザに表示する --> 開発用なので外には公開しない。

Docker や Heroku と同じ起動方法を試すなら gunicorn を使う:

```bash
gunicorn app:app
# PORT 環境変数で待ち受けポートを指定できる (未指定なら 8000)
```

## lint とテスト

```bash
ruff check .
ruff format --check .
pytest
```

CI (GitHub Actions) でもlint・テストと Docker イメージのビルド・起動確認を回している。

## Heroku へデプロイ

```bash
heroku create
git push heroku dev:main
```

Python のバージョンは `.python-version`、起動コマンドは `Procfile` で指定している。
