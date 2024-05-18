def print_params(a, b, c):
    print(a, b, c)

print_params(a = 1, b = 'строка', c = True)

# print_params() , вызов без аргументов.
# ОШИБКА print_params() missing 3 required positional arguments: 'a', 'b', and 'c'

def print_params(a, b, c):
    print(a, b, c)

print_params(a = 1, b = 25, c = True)
print_params(a = 1, b = 'строка', c = [1,2,3])

#print_params(a = 1, b = 'строка', c = [1,2,3], d=34) ОШИБКА лишний параметр
# d=34 лишний параметр, так как в функции только 3 параметра а,в,с.
#print_params(a = 1, b = 'строка') ОШИБКА нехватает параметра. в функции у нас 3 парамнтра а,в,с

def print_params(a, b, c):
    print(a, b, c)

values_list = [34,46] # список распоковался в параметры а,в.
values_dict = {'c': 532} # словарь распоковался в указанный параметр с.
print_params(*values_list, **values_dict)
def print_params(a, b, c):
    print(a, b, c)

values_dict = {'a': 532,'b':89,'c':378 } # словарь распоковался в указанный параметр.
print_params(**values_dict)

def print_params(a, b, c):
    print(a, b, c)

values_list = [34,True,'dog'] # список распоковался в параметры а,в,с. типы данных[int, bool, ctr]

print_params(*values_list)

def print_params(a, b, c,):
    print(a,b,c)

values_list2 = [34,True]
print_params(*values_list2,42) # к данным распакованным добавилось недостающее значение 42,
#заполнились все 3 параметрa.