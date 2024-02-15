from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

from database import create_user, users, check

app = FastAPI()


class MyData(BaseModel):
    name: str
    age: int
    other_id: int


@app.post("/users")
def register(data: MyData):
    if check(data.other_id):
        create_user(data.name, data.age, data.other_id)
        return "successfully registered"
    else:
        return "user already exists"




# @app.get("/users/{name}")
# def get_user(name: str):
#     with open("user.json") as js_file:
#         users = json.load(js_file)
#
#     if name in users:
#         return User(name=str(name))
#     else:
#         return "User not found"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
