import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

#ДЗ lamda функция:
res = map(lambda x, y: x == y, first, second)
print(list(res))


#ДЗ Замыкание:
def get_advanced_writer(file_name):
    if file_name == 'fail_fnl.txt':
        def write_everything(*data_set):
                with open(file_name, 'a', encoding='utf-8') as fail:
                    for data in data_set:
                        fail.write(str(data) + '\n')

        return write_everything


write = get_advanced_writer('fail_fnl.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:
class Multiplier:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        #Если есть такой метод у класса, то его объект можно вызвать как функцию
        return x * self.n


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self, *words):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
