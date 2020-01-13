from typing import Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []


# tags openapi 分组
@app.post(
    "/items/",
    response_model=Item,
    tags=["items"],
    summary="Create an item",  # oepnapi 简介
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",  # 详细描述
    response_description="创建 item",  # 响应描述
)
async def create_item(*, item: Item):
    return item


@app.get("/items/", tags=["items"], summary="函数说明")
async def read_items():
    """
    或者使用函数说明

    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    :return:
    """
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"], deprecated=True)
async def read_users():
    """
    deprecated 已过时
    :return:
    """
    return [{"username": "johndoe"}]
