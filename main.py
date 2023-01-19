from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/write/{value}")
def read_item(value: int, q: Union[str, None] = None):
    with open('data.txt', 'a') as f:
        f.write(f"{value}\n")

    return {"value": value}
