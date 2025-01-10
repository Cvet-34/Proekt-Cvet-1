from fastapi import FastAPI,status, Body, HTTPException, Path
from typing import Annotated, List
from pydantic import BaseModel # Импорт моделей Pydantic (для валидации входящих и исходящих данных)
#модели pydantic проверяют, корректируют дaнные
# или если данные не корректны и нет возможности их скорректировать то выводит исключение-ошибку.


app = FastAPI()

# Создайте пустой список
users = []

# Создание класса(модели) User, от класса BaseModel. Pydantic
class User(BaseModel):
    id: int
    username: str
    age: int

# get запрос по маршруту '/users', который возвращает список users
@app.get('/users')
async def get_users() -> List[User]: # указываем тип User как List[User],
                                        #что позволяет FastAPI проверять,
                                        #что каждый объект в users соответствует модели User
    return users

@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str,
            Path(max_length=35, description='Введите имя', example='Alex')],
        age: Annotated[int,
            Path(le=100, ge=18, description='Введите возраст', example='25')]) -> str:
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return f'Пользователь {user.username} id={user.id} возраст {user.age} зарегестрирован'

@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id: Annotated[int, Path(ge=1, le=100, description='Введите ID', example='1')],
                   username: Annotated[str, Path(max_length=35, description='Введите имя', example='Alex')],
                   age: Annotated[int, Path(le=100, ge=18, description='Введите возраст', example='25')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
        return user
    # исключение в случае отсутствия пользователя с введенным id
    raise HTTPException(status_code=404, detail="Пользователь не найден")

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Введите ID', example='1')]) -> User:
    for user in users:
        if user.id == user_id:
            # удаление записи в списке users по найденному id
            users.remove(user)
            return user
    # исключение в случае отсутствия пользователя с введенным id
    raise HTTPException(status_code=404, detail=f"Пользователь с ID {user_id} отсутствует")