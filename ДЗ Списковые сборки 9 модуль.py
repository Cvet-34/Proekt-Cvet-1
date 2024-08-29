first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
#1. переменную first_result запишите список созданный при помощи сборки
#состоящий из длин строк списка first_strings, при условии, что длина
#строк не менее 5 символов.
first_result = [len(x) for x in first_strings if int(len(x)) >= 5]
print(first_result)
#2.В переменную second_result запишите список созданный
#при помощи сборки состоящий из пар слов(кортежей) одинаковой длины.
#Каждое слово из списка first_strings должно сравниваться с каждым
#из second_strings. (два цикла)
second_result = [(x, y) for x in second_strings for y in first_strings if len(x) == len(y)]
print(second_result)
#3.В переменную third_result запишите словарь
#созданный при помощи сборки, где парой ключ-значение будет
#строка-длина строки. Значения строк будут перебираться из объединённых вместе
#списков first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.

third_result = {x:(len(x)) for x in second_strings + first_strings if len(x) % 2 == 0}
print(third_result)