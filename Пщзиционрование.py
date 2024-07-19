import io
from pprint import pprint
# Работа с курсором ведется в байтах. текст в файле у нас в байтах и перемещение курсора тоже указывать в байтах
name = 'regim2.txt'
file = open(name, 'r', encoding = 'utf-8')
print(file.writable()) # Можем или нет записать что то в этот файл True или False (мы открыли в режиме r чтения, записать не можем False)
print(file.readable()) # Можем считывать информацию в нашем файле. файл открыт в режиме read - r - читать поэтому True
print(file.seekable()) # выводит информацию True или False можем или не можем перемещать курсор в файле метод seek перемещает курсор.
print(file.name) # print(file.   ) и добавляем атрибу что нужно узнать о файле name имя файла, closed закрыт или не закрыт файл и др.
print(file.tell())
pprint(file.read())  # Метод read возвращает положение курсора в нашем файле 0
print(file.seek(9)) # ставим курсор на нужный символ указав сторку, далее чтение будет идти с указанного символа
#pprint(file.read())
file.seek(17)
#file.write('nov tex')
print(file.tell())
#pprint(file.read()) #запускаем чтение еще раз и курсор уходит в самый конец после всех символов
file.close()