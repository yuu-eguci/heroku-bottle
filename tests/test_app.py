import pytest
from webtest import TestApp

from app import app


@pytest.fixture
def client():
    return TestApp(app)


def test_index_says_hello(client):
    response = client.get("/")

    assert response.status == "200 OK"
    assert response.text == "Hello World!"


def test_tpl_renders_template_with_values(client):
    response = client.get("/tpl")

    assert response.status == "200 OK"
    assert response.content_type == "text/html"
    assert "てんぷれーと。aaaabbbb" in response.text


def test_img_page_links_to_static_logo(client):
    response = client.get("/img")

    assert response.status == "200 OK"
    assert '<img src="/static/python-logo.png" />' in response.text


def test_static_logo_is_served_as_png(client):
    response = client.get("/static/python-logo.png")

    assert response.status == "200 OK"
    assert response.content_type == "image/png"
    assert response.body.startswith(b"\x89PNG")


def test_static_rejects_path_traversal(client):
    response = client.get("/static/../app.py", expect_errors=True)

    assert response.status_int == 403


def test_unknown_path_is_404(client):
    response = client.get("/nothing-here", expect_errors=True)

    assert response.status_int == 404
