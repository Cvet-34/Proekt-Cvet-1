# Функция talk(), которая изменяет строку, используя переданный ей объект функции, а затем печатает ее:

def talk(sol):
    ptr = sol(input(" Имя: "))  # вносим имя функцияСодержит имя
    print(ptr)


#Вы можете влиять на полученное сообщение, передавая различные функции:

def pribet(name):
    return f'Привет, {name}'


def poka(name):
    return f'Пока, {name}'


talk(pribet)

talk(poka)
