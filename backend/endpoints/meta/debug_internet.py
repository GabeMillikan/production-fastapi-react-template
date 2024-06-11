import asyncio

import requests
from fastapi.exceptions import HTTPException

from backend.app import app


@app.get("/debug-internet")
async def debug_internet(url: str) -> dict:
    try:
        response = await asyncio.to_thread(requests.get, url)
    except Exception as e:
        raise HTTPException(500, f"ERROR: {e!r}") from e

    return {
        "status": response.status_code,
        "text": response.text,
    }


__all__ = ["debug_internet"]
