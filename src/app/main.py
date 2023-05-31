from datetime import datetime, timezone
from typing import cast

from fastapi import Body, Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl
from sqlalchemy.orm import Session

from .db import ShortUrl, get_db_session
from .service import create_short_url

app: FastAPI = FastAPI()


@app.post("/api/shorten")
def get_short_url(
    db: Session = Depends(get_db_session), url: HttpUrl = Body(..., embed=True)
):
    timestamp = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    short_url = create_short_url(url, timestamp)
    obj = ShortUrl(original_url=url, short_url=short_url)
    db.add(obj)
    db.commit()

    return {"short_url": short_url}


@app.get("/{short_url}")
def redirect(short_url: str, db: Session = Depends(get_db_session)):
    obj = (
        db.query(ShortUrl)
        .filter_by(short_url=short_url)
        .order_by(ShortUrl.id.desc())
        .first()
    )
    if obj is None:
        raise HTTPException(
            status_code=404,
            detail="The link does not exist, could not redirect.",
        )
    return RedirectResponse(url=cast(str, obj.original_url))
