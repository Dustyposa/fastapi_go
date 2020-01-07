from typing import Optional, List
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 限制字符长度
@app.get("/items_limit_length/")
async def read_items_limit_length(
        q: str = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/default/")
async def read_items(q: str = Query("fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/require/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# multi query
@app.get("/mul/")
async def read_items(q: List[str] = Query(None)):
    query_items = {"q": q}
    return query_items


# openapi add desc

@app.get("/o/")
async def read_items(
        q: str = Query(
            None,
            title="查询字符串",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            alias="as",
            deprecated=True  # 废弃
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

