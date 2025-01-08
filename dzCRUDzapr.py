from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

user_db = {'1': "Имя: Example, возраст: 18"}


@app.get("/")
async def get_all_users() -> dict:
    return user_db


@app.get("/user/{user_id}")
async def get_user(user_id: str) -> dict:
    return user_db[user_id]

@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str,
        Path(max_length=30, description='Введите имя', example='Vasiliy')],
        age: Annotated[int,
        Path(le=120, description='Введите возраст', example='20')]
) -> str:
    # присвоение следующего id пользователю
    new_user_id = str(int(max(user_db, key=int)) + 1)
    # добавление в users
    user_db[new_user_id] = f'Имя: {username}: Возраст: {age}'
    return f'Пользователь {new_user_id} зарегестрирован'


@app.put('/user/{user_id}/{username}/{age}')
async def put_users(
        user_id: int,
        username: Annotated[str,
        Path(max_length=30, description='Введите свое имя', example='Vasiliy')],
        age: Annotated[int,
        Path(ge=18, le=120, description='Введите возраст', example='24')]) -> str:
    user_db[user_id] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь {user_id} обновлен'


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    user_db.pop(user_id)
    return f"Пользователь {user_id} удален."

