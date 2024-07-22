def f1 (number):
    return 10/number
def f2 ():
    print('какой хороший день')
    result_f1 = f1(0)
    return result_f1
try:
    total = f2()
    print(total)
except ZeroDivisionError as exc:
    print(f'вот что то не так-{exc} но мы устояли')

def f1 (number):
    return 10/number



def f2 ():
    print('какой хороший день')
    summ = 0
    for i in range(-2, 2):
        summ += f1(i)
    print(summ)
    return summ

try:
    total = f2()
    print(total)
except ZeroDivisionError as exc:
    print(f'что то не так-{exc}, но мы устояли')


def f1 (number):
    return 10/number



def f2 ():
    print('какой хороший день')
    summ = 0
    for i in range(-2, 2, 1):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'внутри f1 что то пошло не так: {exc} но программа живая, мы молодцы')
    return summ/0

try:
    total = f2()
    print(f'вот ваш результат функции:, {total}')
except ZeroDivisionError as exc:
    print(f'что то не так-{exc}, но мы устояли')



def f1 (number):
    return total / number


def f2 ():
    print('какой хороший день')
    summ = 0
    for i in range(-2, 2, 1):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'внутри f1 что то пошло не так: {exc} но программа живая, мы молодцы')
    return summ/0

try:
    total = f2()
    print(f'вот ваш результат функции:, {total}')
except ZeroDivisionError as exc:
    print(f'что то не так-{exc}, но мы устояли')


def f1 (number):
    return total / number


def f2 ():
    print('какой хороший день')
    summ = 0
    for i in range(-2, 2, 1):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as exc:
            print(f'внутри f1 что то пошло не так: {exc} но программа живая, мы молодцы')
    return summ/0

try:
    total = f2()
    print(f'вот ваш результат функции:, {total}')
except NameError as exc:
    print(f'что то не так-{exc}, но мы устояли')
