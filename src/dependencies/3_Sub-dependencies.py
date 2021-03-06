from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str = None):
    return q + "str"


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: str = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}


async def needy_dependency(fresh_value: str = Depends(query_or_cookie_extractor, use_cache=False)):
    """use_cache取消缓存"""
    return {"fresh_value": fresh_value}
