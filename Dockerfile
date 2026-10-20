FROM python:3.15-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd --create-home app
USER app

EXPOSE 8080
# gunicorn binds to 0.0.0.0:$PORT when PORT is set, so Heroku's PORT is honoured too.
CMD ["gunicorn", "app:app"]
