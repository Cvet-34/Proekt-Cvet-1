#try:
    # пишем здесь код с возможной ошибкой
#except:
    # пишим здесь блок кода в случае возникновения ошибки

#try:
    #i = 0
    #print(10/i)
    #print('сделано')
#except ZeroDivisionError:
    #print('нельзя делить на ноль!')

#try:
    #truba = a + b # ошибка NameError,
    #truba = 10/0 # ошибка ZeroDivisionError на 0 делить нельзя
#except (ZeroDivisionError, NameError): #Указали имени классов ошибок. в данном случае низнаем из за какой ошибки вышло предупреждение.
    #print('что то пошло не так, но мы устояли')

# Создаем несколько блоков  except для отображения предупреждений по назным ошибкам
#try:
    #truba = a + b # ошибка NameError,
    #truba = 10/0 # ошибка ZeroDivisionError на 0 делить нельзя
#except ZeroDivisionError: #Указали имени классов ошибок. в данном случае низнаем из за какой ошибки вышло предупреждение.
    #print('Они делили на ноль, но мы не упали')
#except (NameError): #Указали имени классов ошибок. в данном случае низнаем из за какой ошибки вышло предупреждение.
    #print('нет такой переменной, кто писал этот код?!')

#try:
    #a = 10/0 # ошибка ZeroDivisionError на 0 делить нельзя
#except ZeroDivisionError as exc: # пишем имя классов ошибки и переменную в которой будет уточнение что за ошибка
    #print(f'что то пошло не так - {exc}, но мы устояли') # получаем в консоль - "что то пошло не так - division by zero, но мы устояли"

#try:
    #file = open('test123.txt')
#except OSError as exc:  #Исключение связано с ОС
    #print(f'вот что пошло не так - {exc} параметры {exc.args}, но мы еще на праву')

print('----Какой хороший день, предлагаю научиться работать с исключениями - ')
i = int(input('Введите число: '))

try:
    result = 10* (1/i)
except ZeroDivisionError as exc:
    print('нельзя делить на ноль!', exc)
else:
    print('ура, мы не делить на ноль')
finally:
    print('финал мы заканчиваем урок :)')


