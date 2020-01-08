from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: List[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


# Don't do this in production!
@app.post("/user/", response_model=UserIn)
async def create_user(*, user: UserIn):
    return user


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


@app.post("/user_out/", response_model=UserOut)
async def create_user_out(*, user: UserIn):
    return user


class Items(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Items, response_model_exclude_unset=True)
async def read_itema(item_id: str):
    """response_model_exclude_unset 取消返回默认值"""
    return items[item_id] if item_id in items else Items(name="asd", price=0.0)


class Ite(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5


ite = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Ite,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return ite[item_id]


@app.get("/items/{item_id}/public", response_model=Ite, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return ite[item_id]
