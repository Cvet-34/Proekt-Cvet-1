import io
from pprint import pprint
# Работа с курсором ведется в байтах. текст в файле у нас в байтах и перемещение курсора тоже указывать в байтах
#name = 'regim2.txt'
#with(open(name, encoding = 'utf - 8')) as file:
    #for line in file:
        #print(line, end='')

name = 'regim2.txt'
with(open(name, encoding = 'utf - 8')) as file: #для упрощения рабты с файлами
    for line in file:
        for char in line:
            print(char, end='') # с end текст в троку распределен гармонично

name = 'regim2.txt'
with(open(name, encoding = 'utf - 8')) as file:
    for line in file:
        for char in line:
            print(char)  # без end текст по симовольно в столбец
    print(file.tell())
# при работе с with  как тольк действия с отступом заканчиваются работа с файлом заканчивется и файл закрывается.
#дополнительно закрывать не нужно.
# все что с отступов после with принадлежит  with и выполняется. как только отступы закончены программа закончена.
# и если мы снова захотим считать файл print(file.read()) получим ошибку так как файл закрыт и мы не можем читать его.