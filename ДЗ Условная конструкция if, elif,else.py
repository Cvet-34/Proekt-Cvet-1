# первый вариант все заначения равны.
first = 123
second = 123
third = 123

if first == second or second == third or third == first: # or достаточно выполнения одного значения
    print('первый ваниарт ответ:', 2)
if first == second == third:
    print('первый ваниарт ответ:', 3)
else:
    print('первый ваниарт ответ:', 0)
#При таких условиях ответ в консоли 2, 3.


# Второй вариант не все значения равны.
first = 12
second = 123
third = 123

if first == second and second == third and third == first: #для выполения условия все значения должны быть равны
    print('второй ваниарт ответ:', 2)
elif first == second == third:
    print('второй ваниарт ответ:', 3)
else:
    print('второй ваниарт ответ:', 0)


# Третий вариант не все значения равын. но применяя  or проверка при ответе 2 хотябы одно равенство верно.
first = 12
second = 123
third = 123

if first == second or second == third or third == first: # остаточно одного равинстав  second == third
    print('третий ваниарт ответ:', 2)
elif first == second == third:
    print('третий ваниарт ответ:', 3)
else:
    print('третий ваниарт ответ:', 0)
