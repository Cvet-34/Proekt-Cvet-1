if 1:
    print('Hello 1')

a = 3
if a == 3:
    print('Hello 3')

a = 3
if a > 1:
    print('Hello, 4')

ist = [1, 2, 3, ]
if ist:
    print('hello,5')

a = -3
if a < 1:
    print('Hello, 6')

a = 1
if a > 2:
    print('H')
else:
    print('R')

a = 3
if a > 2:
    print('H')
else:
    print('R')

a = 9
b = True
if a > 10:
    print(b)
else:
    print(False, 1)

a = 17
b = True if a > 10 else False
print(b)

a = int(input('Введите число'))
if a > 0:
    print('hHeg')
elif a == 0:
    print('Zero')
else:
    print('Pos')

# цикл while
a = 0
while a < 7:
    print('A')
    a += 1

a = 0
while a == 0:  # пример бесконечного цикла.
    print('B')
    break  # Останавливает цикл. цикл выполнится только 1 раз и остановится.

а = 0
while a >= 0:
    if a == 7:
        break
    a += 1
    print('O')

# Оператор continue.
# Оператор continue запускает цикл заново, при этом код, расположенный после данного оператора, не выполняется.
a = -1
while a < 10:
    a += 1
    if a >= 8:
        continue
    print('p')

# for

for i in range(5):  #range (start, stop, step) в этом примере start (5)
    print('Hello')  #Печатается 5 раз цикл for сработает 5 раз

lst = [1, 2, 3, 4, 5]  # список lst Цикл фор пройдет по списку 5 раз по количеству элементов в списке
for i in lst:  #цикл for через i переберает список lst и далее в print выполняется действие
    print(i ** 2)  # возвести в квадрат. напечатать число.

word_str = "Hello, world!"  #Можно пробежать циклом фор повсем элементов в текстовой строке.
for l in word_str:
    print(l)  # распечатается каждый элемент текста

name = ['Иван', 'ваня', 'ванюша']
if 'ваня' in name:
    print('hello!')
