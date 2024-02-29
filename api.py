from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

from database import create_user, check, return_user, check_link

app = FastAPI()


class UserData(BaseModel):
    name: str
    other_id: int
    link_to_git: str


class UserMassage(BaseModel):
    text: str
    link_to_git: str


@app.post("/users")
def register(data: UserData):
    if check(data.other_id):
        create_user(data.name, data.link_to_git, data.other_id)
        return "successfully registered"
    else:
        return "user already exists"


@app.post("/text")
def text(text: UserMassage):
    if check_link(text.link_to_git):
        return "123"
        # записываешь в бд


@app.post("/users/{id}")
def register_message(id: int):
    return return_user(id)


@app.post("/users/text/{id}")
def returned_text(id: int):
    return return_text(id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
