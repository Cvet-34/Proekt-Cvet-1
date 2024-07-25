# пример 2  Пример списковой сборки
# аналог map

#List_comp_1 = [x*2 for x in collection]


#пример
my_nambers = [3, 1, 4, 1, 5, 9, 2, 6]
result = [x * 3 for x in my_nambers]
print(result)

#пример 3 списковая сборка
#аналог filter

my_nambers = [3, 1, 4, 1, 5, 9, 2, 6]
result = [x * 3 for x in my_nambers if
          x % 2]  # x*3 нвчение с которым идет работа, for цикл, if условие только не четные числа
print(result)

my_nambers1 = [3, 1, 4, 1, 5, 9, 2, 6]  # пример функции которые были ранее
for x in my_nambers1:
    result = x * 3
    if x % 2:  # фильтрация. умножаются на 3только те значения которые не четные и не делятся на 2 без остатка.
        print(result)

#Пример 4. Условие перед циклом. поменять оберацию для работы с данными списка

my_nambers = ['A', 1, 4, 'B', 5, 'C', 2, 6]

result = [x if type(x) == str else x * 5 for x in my_nambers]  # не отфильтровать, а поменять операцию над этими значениями

print(result)

# Пример 4.
my_nambers = [3, 1, 4, 1, 5, 9, 2, 6]
they_nambers = [2, 7, 1, 8, 2, 8, 1, 8, ]

result = [x * y for x in my_nambers for y in they_nambers]  # вычисления
print(result)

result = [x * y for x in my_nambers for y in they_nambers if
          x % 2]  #вычисления и фильтрация X. умножение после фильтрации
print(result)

result = [x * y for x in my_nambers for y in they_nambers if
          x % 2 and y // 2]  #вычисление и фильтрация Х и У. умножение после фильтации
print(result)

# можно так же генерировать множества и словари
my_numbers = [3, 1, 4, 1, 5, 9, 2,
              6]  # множество содержит только уникальные значения, повторов нет. после вычислений выходит упорядоченный список, повторы удаляются.
result = {x for x in my_numbers}
print(result)

they_nambers = [3, 1, 4, 1, 5, 9, 2, 6]  #словарь
result = {x: x ** 2 for x in my_numbers}
print(result)
