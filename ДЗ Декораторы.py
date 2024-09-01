# число является простым если делится на 1 и на себя например число 7
# Число является составным если делится на разнве делители например 12 делится на 2 на 3 и др

def is_prime(func):  #функция проверяет и выводит простое число.
    def decor():
        n = func()
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        return 'Простое число' if count == 2 else 'Составное число'

    return decor


@is_prime
def sum_three():
    a = 5 + 5 + 1
    print(a)
    return a


print(sum_three())
