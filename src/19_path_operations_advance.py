from typing import Set

from fastapi import FastAPI
from fastapi.routing import APIRoute
from pydantic import BaseModel

app = FastAPI()


@app.get("/items/", operation_id="some_specific_id_you_define")
async def read_items():
    return [{"item_id": "Foo"}]


@app.get("/ite/", include_in_schema=False)
async def read_ite():
    """
    include_in_schema 是否展示在 api web中
    :return:
    """
    return [{"item_id": "Foo"}]


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []


@app.post("/item/", response_model=Item, summary="Create an item")
async def create_item(*, item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    \f
    \f 文档截断，以下不会出现在文档中
    :param item: User input.
    """
    return item


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    设置OpenAPI operation id
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'


use_route_names_as_operation_ids(app)
