from datetime import datetime
from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "Dusty posa"
    signup_ts: datetime = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2020-01-05 19:33",
    "friends": [1, "2", b"3", 4.5, 2],
}

user = User(**external_data)
print(user)

print(user.id)
