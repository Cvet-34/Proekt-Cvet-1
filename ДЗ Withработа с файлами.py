import io
from pprint import pprint

name = 'dz_with.txt'                        # Название файла с текстом
with open(name, encoding='utf-8') as file:  # открыли файл 'dz_with.txt' с помощью оператора with
    for line in file:
        for chang in line:
            print(chang, end='')
    print(file.tell())
    # если файл открыт с помощью оператора with то закывать специально не нужно. закрывается автомотически. работает только то что с отступом в зоне with.
    #если с начала строки без отступа значит к with  не принадлежит и файл закрыт. и нет возможности рабатать с файлом.
print(file.read())