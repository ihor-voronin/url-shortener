from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.post("/api/shorten")
def get_short_link():
    return {"short_link": "short_link"}


@app.get("/{short_link}")
def redirect():
    return RedirectResponse(url="google.com")
