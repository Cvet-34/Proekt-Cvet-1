import fastapi
from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def welcome1() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def news(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID'", example="1")]) -> dict:
        return {"massage": f"Hello, {user_id}"}


@app.get("/user/{username}/{age}")
async def news(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Urban User")]
                   , age: int = Path(ge=18, le=20, description="Enter age", example="24")) -> dict:
        return {"massage": f"Hello, {username}:{age}"}


