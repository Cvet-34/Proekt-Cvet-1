import sqlite3
import random

connection = sqlite3.connect("not_telegram.db") # контакт, обращение к базе данных через sqlite3.connect
cursor = connection.cursor() #для указания каждой ячейки нужен курсор, объект который умеет взаимодействовать с базой данных
# создаем файл для базы данных, записываем по каким данным строится таблица
# далее используем команду execute помогает напрямую обращаться и передавать данные в нашу БД. далее пишем SQL запросы в БД.
cursor.execute('''  
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# позволяет создать индекс для (email)
#cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
#Заносим данные в таблицу, проверка
#cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", ("User", "exam@gmail.com", 10, 1000))
#делаем 10 экземплянов записей под своим номером
#for i in range(10):
    #i += 1
    #cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{0+i}", f"example{i}@gmail.com", f"{i*10}", 1000))
#Удалили лишний "User"
#cursor.execute("DELETE FROM Users WHERE username = ?", ("User",))

# Изменили каждую 2ую запись в balance на 500
#for i in range(10):
    #cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i*2}"))

#cursor.execute("DELETE FROM Users WHERE username = ?", ("User1",))
#cursor.execute("DELETE FROM Users WHERE username = ?", ("User4",))
#cursor.execute("DELETE FROM Users WHERE username = ?", ("User7",))
#cursor.execute("DELETE FROM Users WHERE username = ?", ("User10",))

# SELECT может получать данные из БД
# ищем определенные данные в нашей базе данных
#Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
#cursor.execute("SELECT username, age FROM Users WHERE age != ?", (60,))
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(user)


connection.commit() # сохранить состояние БД
connection.close() # закрыть подключение после всей работы с БД
















