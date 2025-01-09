from fastapi import FastAPI,status, Body, HTTPException, Path
from typing import Annotated, List
from pydantic import BaseModel # Импорт моделей Pydantic (для валидации входящих и исходящих данных)
#модели pydantic проверяют, корректируют динные
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
            Path(max_length=30, description='Введите имя', example='Vasay')],
        age: Annotated[int,
            Path(le=2000, description='Введите возраст', example='200')]):
    user_id = len(users) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return f'Пользователь {user.username} id={user.id} возраст {user.age} зарегестрирован'

@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id: Annotated[int, Path(description='Введите ID', example='1')],
                   username: Annotated[str, Path(max_length=30, description='Введите имя', example='Vasay')],
                   age: Annotated[int, Path(le=1000, description='Введите возраст', example='200')]):
    for i in users:

        if i.id == user_id:
            i.username = username
            i.age = age
        return users  # возвращает обновленный список
    # исключение в случае отсутствия пользователя с введенным id
    raise HTTPException(status_code=404, detail="Пользователь не найден")


@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(description='Введите ID', example='1')]):
    for i, user in enumerate(users):
        if user.id == user_id:
            # удаление записи в списке users по найденному id
            del users[i]
            return users # возврат измененный список users
    # исключение в случае отсутствия пользователя с введенным id
    raise HTTPException(status_code=404, detail=f"Пользователь с ID {user_id} отсутствует")