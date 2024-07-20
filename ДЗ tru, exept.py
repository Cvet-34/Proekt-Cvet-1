
print('Пример:1')
try:
    a = 123  # тип int
    b = 'яблоко'  # тип str
    add_everything_up = a + b
    print(add_everything_up)
except TypeError:    # имя ошибки
        print(a, b)

finally:
        print('разные типы данных int, str, сложение невозможно!')

print('Пример:2')
try:
    a = 123.456                 # тип float
    b = 7                       # тип int
    add_everything_up = a + b
    print(add_everything_up)

except TypeError as exc:
        print(a, b, exc)
else:
        print('все работает хорошо')
finally:
        print('типы данных подлежат сложению!')

print('Пример:3')
try:
    a = 123.456     # float
    b = 'огонь'         # str
    add_everything_up = a + b
    print(add_everything_up)

except TypeError as exc: # exc подсказывает нам по какой причине произошла ошибка
        print(a, b, exc)
else:
        print('все работает хорошо') # Так как проявилась ошибка, то это сообщение не выводится. выводится только если все норм.
finally:
        print('Внимание!Разные тимы данных! Обратите внимание на справку в консоли')