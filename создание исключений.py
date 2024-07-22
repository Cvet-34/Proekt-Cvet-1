# Пример 1 raise.

#def greet_person(person_name):
#if person_name == "ВолонДеМорт":
#raise Exception('Мы нелюбим ВолонДеМорт')
#print(f'Привет, {person_name}')

#greet_person('Дорогой ученик')
#greet_person('ВолонДеМорт')

# Пример 2
#try:
#    raise NameError('Привет Там')
#except NameError as exc:
#    print((f'Исключение типа {type(exc)} пролетело мимо! его параметры {exc.args}'))
#    raise

# Работа с классом Exception. в Exception вложены методы для создания исключений и ошибок если необходимо.

class Exсeption:
    pass


#Пример 3
#class ProZero(Exception):
#    pass

#def f(a,b):
#    if b == 0:
#        raise ProZero('Деление на ноль невозможно')
#    return a/b

#print(f(5,0))

class ProZero(Exception):
    def __init__(self, massege, extra_info):
        self.massege = massege
        self.extra_info = extra_info

def f(a, b):
        if b == 0:
            raise ProZero('Деление на ноль невозможно', {"a": a, "b": b})
        return a / b

try:
    result = f(10, 2)
    print(result)
except ProZero as e:
    print('Не очень хорошо, ошибка')
    print(f'сообщение об ошибке: {e.massege}')
    print(f'Дополнительная информация: {e.extra_info}')
