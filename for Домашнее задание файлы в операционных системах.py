import os
import time

file1 = 'fileOP.txt'
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = (r'C:\PythonProject ДЗ1 Открытие файлов\pythonProjectфайлы в операционной системе лекция\модуль 7\fileOP.txt')
        filetime = os.path.getmtime(r'C:\PythonProject ДЗ1 Открытие файлов\pythonProjectфайлы в операционной системе лекция\модуль 7\fileOP.txt')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesiz = os.path.getsize(r'C:\PythonProject ДЗ1 Открытие файлов\pythonProjectфайлы в операционной системе лекция\модуль 7\fileOP.txt')
        parent_dir = os.path.dirname(r'C:\PythonProject ДЗ1 Открытие файлов\pythonProjectфайлы '
                            r'в операционной системе лекция\модуль 7\fileOP.txt')
print(f'Обнаружен файл: {file1}, Путь: {filepath}, Размер: {filesiz} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
