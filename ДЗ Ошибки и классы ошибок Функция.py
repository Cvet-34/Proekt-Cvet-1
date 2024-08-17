def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError as exc:  # имя ошибки
        print(f'ОШИБКА! {exc} тип данных не подлежит сложению, подробно от ошибке {exc.args}')
    else:
        print('все работает хорошо, типы данных подлежат сложению')
    finally:
        print('Программа завершена')


#print(add_everything_up(123.456, 'строка'))
#print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
