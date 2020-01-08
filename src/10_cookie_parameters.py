from typing import List

from fastapi import Cookie, FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
        *,
        ads_id: str = Cookie(None),
        user_agent: str = Header(None),
        stranger_agent: str = Header(None, convert_underscores=False)
):
    """convert_underscores 禁止下划线转-"""
    return {"ads_id": ads_id, "user_agent": user_agent, "stranger_agent": stranger_agent}


# duplicate header

@app.get("/d/")
async def read_items(x_token: List[str] = Header(None)):
    return {"X-Token values": x_token}

