from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional

# import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "sara"}}


@app.get("/blog")
def blog(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # Fetches blog by the 'id'
    if published:
        return {"data": f"{limit} published blogs"}
    else:
        return {"data": f"{limit} blogs"}


@app.get("/blog/{id}")
def blog(id: int):
    # Fetches blog by the 'id'
    return {"blog": id}


@app.get("/blog/{id}/comments")
def comments(id: int, limit: int = 10):
    # Fetches comments of the blog by the 'id'
    return {"id": id, "comments": limit}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog '{request.title}' created!"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
