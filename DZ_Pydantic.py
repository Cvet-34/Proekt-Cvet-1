import fastapi
from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List



app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int, user_id: int) -> str:
    username.user_id = len(users)
    users.append(username)
    users.age = len(users)
    users.append(age)
    return f"User {user_id+1} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def updata_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_username = users[user_id]
        edit_username.str = username, age
        return f"The user {user_id} is registered"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"Message with {user_id} was deleted."
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")
