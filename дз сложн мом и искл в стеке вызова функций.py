def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
            print(i)
            result += i
        print(result)
    except TypeError as exc:
        print(f'не верный тип данных {exc} подробнее {exc.args}')
        incorrect_data += 1
        print()
    return result, incorrect_data

def calculate_average(numbers):
    try:
        a = sum(numbers) / len(numbers)
        print(a)
        summ = 0
        for i in range(numbers):
            summ += personal_sum()
            print(summ)
    except ZeroDivisionError as exc:
        print(f'Делить на ноль нельзя', exc)
    except TypeError as exc2:
        print(f'не верный тип данных', exc2)



print(f'Решение 1: {personal_sum("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Решение 2: {personal_sum([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Решение 3: {personal_sum(567)}')  # Передана не коллекция
print(f'Решение 4: {personal_sum([42, 15, 36, 13])}')  # Всё должно работать


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать

