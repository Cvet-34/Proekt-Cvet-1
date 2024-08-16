import os
import time

print('Текущая дируктория:', os.getcwd())  # смотрим путь где находимся
#os.mkdir('novay')  # создание папки новой
if os.path.exists('novay'):  #если существует 'novay'
    os.chdir('novay')  # изменяем
else:  # Если нет директории то будем создавать ее и измениять
    os.mkdir('novay')  #создавать
    os.chdir('novay')  #измениять
print('Текущая дируктория:', os.getcwd())  # смотрим путь где находимся
#os.makedirs(r'pervai\vtoray')
print(os.listdir())  # Видим только частично папку
for i in os.walk('.'):  # Смотрим вложенность целеком что есть в директории, '.' - текущая директория
    print(i)  # выводим значение i взятая информация из директории
os.chdir(
    r'C:\PythonProject ДЗ1 Открытие файлов\pythonProjectфайлы в операционной системе лекция\модуль 7')  # добавляем 'r чтоб небыло ошибки
print('Текущая дируктория:', os.getcwd())  # смотрим путь где находимся os.getcwd()) какая сейчас рабочая директория
print(os.listdir())  #смотрим какие папки вообще есть не отсортированы
file = [f for f in os.listdir() if
        os.path.isfile(f)]  # генератор метод isfile будет возвращать Trye усли мы указали файлы
dirs = [d for d in os.listdir() if
        os.path.isdir(d)]  # # генератор метод isdir будет возвращать Trye усли мы указали директорию
print(dirs)  # выводим в консоль смотрим какие директории есть по порядку
print(file)  #выводим в консоль смотрим какие файлы есть
os.startfile(file[0])  #  смотрим текстовый файл под индексом [0] fileOP.txt содержимое текстового документа
print(os.stat(file[0]))  # вся информация о файле например время начала создания файла, когда был изменен и др.
print(os.stat(
    file[0]).st_size)  #чтобы получить конкретные данные обращаемся к конкретному атрибуту st_size - размер файла
#os.system('pip install random2')
#print(os.path.join([0]))
path1 = 'novay'
path2 = '12345'
path3 = 'fileOP.txt'
result = os.path.join('novay', '12345', 'fileOP.txt') # объединяем компоненты в единый путь
print(result)

print(os.path.getmtime(r'C:\PythonProject ДЗ1 Открытие файлов\pythonProjectфайлы ' # время последней модификации файла в секундах с пл.точк
                       r'в операционной системе лекция\модуль 7\fileOP.txt'))
mtime = os.path.getmtime(r'C:\PythonProject ДЗ1 Открытие файлов\pythonProjectфайлы '
                         r'в операционной системе лекция\модуль 7\fileOP.txt')
print(time.ctime(mtime)) # преобразует секунды в данные даты, время. создания файла.
print(os.path.getsize(r'C:\PythonProject ДЗ1 Открытие файлов\pythonProjectфайлы '
                            r'в операционной системе лекция\модуль 7\fileOP.txt')) # getsize возвращает размер файла в байтах
print(os.path.dirname(r'C:\PythonProject ДЗ1 Открытие файлов\pythonProjectфайлы '
                            r'в операционной системе лекция\модуль 7\fileOP.txt')) # получаем путь к родительской директории файла.