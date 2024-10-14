import fastapi
from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/user")
async def get_all_messages() -> dict:
    return users


@app.post("/user/{username}/{age}'")
async def create_message(username, age: str, user_id: str) -> str:
    current_index = str(int(max(users, key=int)))
    users[current_index] = username, age
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}'")
async def updata_message(user_id, username, age: str, user: str) -> str:
    user[user_id, username, age] = user
    return f"The user {user_id} is registered"


@app.delete("/user/{user_id}")
async def delete_message(user_id: str) -> str:
    users.pop(user_id)
    return f"Message with {user_id} was deleted."
