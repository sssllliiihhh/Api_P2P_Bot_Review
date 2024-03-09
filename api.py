from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

from func import apifunc

app = FastAPI()


class UserData(BaseModel):
    name: str
    other_id: int
    link_to_git: str


class UserMassage(BaseModel):
    text: str
    link_to_git: str
    other_id: int


# Миша
@app.post("/users")
def register(data: UserData):
    return apifunc.register_user(data)

# Даша
@app.post("/text")
def text(text: UserMassage):
    return apifunc.register_text(text)

# Марк
@app.get("/queue/{id}")
def queue(id):
    return apifunc.return_queue(id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
