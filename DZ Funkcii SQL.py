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

#cursor.execute("DELETE FROM Users WHERE username = ?", ("User6",)) #Удалили ппользователя User6

cursor.execute("SELECT COUNT(*) FROM Users") # Посчитали общее количество записей в списке 5.
zapisi = cursor.fetchone()[0]
print(zapisi)

cursor.execute("SELECT SUM(balance) FROM Users") # сумма общего balance
balanss = cursor.fetchone()[0]
print(balanss)

print(balanss/zapisi)


connection.commit() # сохранить состояние БД
connection.close() # закрыть подключение после всей работы с БД



