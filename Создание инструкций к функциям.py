#Примеры функций с инструкциями

#Функции простые
#Функции принимающие
#Функции принимающи и возвращающие результать в программу
#Функцич определяется с помощью ключевого слова def ...

#def hello():  # простая функция
#print('Hello, CBETA')

#hello()

# Создание функций с if, else.
#def names(): # функция прописаны условия ввод имени, если есть в имени гласные то есть если нет то нет.
#name = str(input('Введите ваше имя '))
#if set('aeiou').intersection(name.lower()):
#print('В вашем имени есть гласные буквы')
#else:
#print('Ваше имя не содержит гласных букв')
#for letter in name: #цикл фор пробегает по имени ищя гласные сопостовляя с условием и переберая список находит или не находит гласн.
#print(letter)

#names()

#далее:
#Функция с параметрами принимиющая
#Рассмотрим функцию с параметрами i, j, k и сложение их данных в разных конфигурациях

def add(i, j, k):
    q = i + j
    w = i + k
    e = j + k
    print(q, w, e)


add(20, 25, 30)


def add1(a, b, c):  # функция сложения, принимающая данные для параметров и примениящая их для сложения пареметров.
    e = a + c
    f = b + c
    r = b + a + c
    ra = r + a + e
    print(e, f, r, ra)


add1(11, 23, 15)


# Функция с параметрами
#def info(name, age):
#print('Name:' + name)
#print('Adg:' + str(age))


# Определение функции с параметрами
def info(name, age):
    print("Имя: " + name)
    print("Возраст: " + str(age))


#Вызов функции с параметрами выше
info('CBETA', 25)
info('OLA', 34)

#Вызов функции с использованием ключевых аргументов
info(name='CACHA', age=28)


def info2(name, rost):
    print('имя: ' + name)
    print('рост: ' + str(rost))


info2('Петр', 180)
info2(name='Сергей', rost=185)


#Определение функции с параметрами
#Присвоение ключевых аргументов

def infon(name, age=20):
    print('Имя:' + name)
    print('Возраст:' + str(age))


#Вызов функции с ключевым аргументом и без ключевого аргумента

infon(name='СВЕТА')
infon(name='ОЛЬГА', age=25)


#Возвращение значений
#Значение параметра можно возвращать с помощью оператора return.
def testn(i):
    j = i ** 3
    return j


result = testn(5)
print(result)


def testo(i):
    a = (i + 8) * 2


#    return a


res = testo(2)
print(res)


#Рассмотрим возвращение функции с помощью return
def addr(i, j, k):
    q = i + j
    w = i + k
    e = j + k
    return q, w, e


result = addr(20, 25, 30)
print(result)


def adr(i, j, k):
    a = i * 5
    b = j + k
    c = k % 2
    return a + b + c


result = adr(5, 7, 6)
print(result)


def asd(a, b, c, d):
    q = a * 3
    w = a + b + c * d
    r = c // 2
    t = d + 4
    return q, w, r, t


result = asd(3, 12, 5, 6)
print(result)


#Функция main() помещает в себя компоненты программы в одну функцию,
#в то же время функцию main() не обязательно вызывать в программе.
def testmain():
    print('Hello, OGGO, PPP')


def main():
    print('This is test text')


testmain()
main()

# Объявление глобальной переменной и для ввода имени

name = str(input('Ваше имя: '))


# Функция для проверки гласных букв
def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print('В вашем имени есть гласные буквы')

    else:
        print('В вашем имени нет гласных букв.')
        print('В вашем имени нет гласных букв.')


# Итерация букв в имени
def print_letters():
    for letter in name:
        print(letter)


# Определение главной функции
def main():
    has_vowel()
    print_letters()


# Выполнение функции main
if __name__ == '__main__':
    main()



