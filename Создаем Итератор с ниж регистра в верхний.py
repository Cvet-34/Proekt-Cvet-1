# последовательно напечатать числа от 1 до 999

#for i in range(1,100):
#  print(i)

##############################
#Создадим простой строковый итератор, который на каждой итерации, при получении следующего элемента
# (т.е. символа), приводит его к верхнему регистру:
class ToUpperCase:
    def __init__(self, string_obj, position = 0):
        """сохраняем строку, полученную из конструктора,
                в поле string_obj и задаём начальный индекс"""
        self.string_obj = string_obj
        self.position = position

    def __iter__(self):
        """ возвращаем сам объект """
        return self

    def __next__(self):
        """ метод возвращает следующий элемент, но уже приведенный к верхнему регистру """
        if self.position >= len(self.string_obj):
            # исключение StopIteration() сообщает циклу for о завершении
                raise StopIteration()
        position = self.position
            # инкрементируем индекс
        self.position +=1
            # возвращаем символ в uppercase-e
        return self.string_obj[position].upper()


# обращение к функциям

low_pyton = 'pyton'
high_python = ToUpperCase(low_pyton)
for ch in high_python:
    print(ch, end="")

# В итоге выводится в консоль : PYTON