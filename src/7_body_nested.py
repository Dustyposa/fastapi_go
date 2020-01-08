from typing import List, Set

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: list = []


class It(Item):
    tags: List[str] = []


class Ite(Item):
    tags: Set[str] = set()


@app.put("/i/{item_id}")
async def update_item(*, item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/it/{item_id}")
async def update_item(*, item_id: int, item: It):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/ie/{item_id}")
async def update_item(*, item_id: int, item: Ite):
    results = {"item_id": item_id, "item": item}
    return results


class Image(BaseModel):
    url: HttpUrl
    name: str


class Itm(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []
    image: Image = None


class Itmg(Itm):
    images: List[Image] = None


@app.put("/itM/{item_id}")
async def update_item(*, item_id: int, item: Itm):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/itg/{item_id}")
async def update_item(*, item_id: int, item: Itmg):
    results = {"item_id": item_id, "item": item}
    return results
