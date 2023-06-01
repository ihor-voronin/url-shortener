from fastapi.testclient import TestClient

from app.main import app


def test_main():
    with TestClient(app) as client:
        url = "https://google.com"
        response = client.post(
            "/api/shorten",
            headers={"Content-Type": "application/json"},
            json={"url": url},
        )

        assert response.status_code == 200
        assert "short_url" in response.json()
        short_url = response.json()["short_url"]
        assert len(short_url) == 7

        response = client.get("/{}".format(short_url), follow_redirects=False)
        assert response.status_code == 307
        assert response.headers["Location"] == url

        response = client.get("/non-existing-path", follow_redirects=False)
        assert response.status_code == 404
