import fastapi
from fastapi import FastAPI

app = FastAPI() # далее включино в декоратор для функции


#Конечные точки API в Python
#— это общедоступные URL-адреса, предоставляемые сервером, которые
#клиентское приложение использует для доступа к различным ресурсам и данным.

@app.get("/") #если получили get запрос то обаработай нам функцию welcome
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def welcome() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def welcome(user_id: str) -> dict:
    return {"message": f"Вы вошли как пользователь №, {user_id}"}



@app.get("/user")
async def welcome() -> dict:
    return {"message": " Информация о пользователе. Имя: Ольга, Возраст: 23 "}

