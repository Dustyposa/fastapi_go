from fastapi import Depends, FastAPI, Header, HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED


app = FastAPI()


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")

    return JSONResponse(status_code=HTTP_201_CREATED, content={"ok": 1})  # not useful
    # return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]