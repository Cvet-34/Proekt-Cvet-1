info = [  # исходные данные
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']


def custom_write(fail_name, string):
    global i
    file = open(fail_name, 'a', encoding='utf-8')  # открыли файл для записи "а".
    print(file.tell())  # определяем 0 байт
    a = file.tell()  # Фиксируем значение 0 байтов в переменной
    file.write('Text for tell.,')  # через write записываем первую строку текста
    print(file.tell())  # определяем конечный байт первой строки
    b = file.tell() + 1  # конечный байт первой строки 15 + 1 = 16. 16 начало сл строки фикс.знач
    file.write('\nИспользуйте кодировку utf-8.')  # печатаем вторую строку в текстовый файл
    print(file.tell())  # определяем байты конца второй строки
    c = file.tell() + 1  # конечный байт 2ой строки 65 + 1 = 66 вычеслили начало 2ой строки
    file.write('\nBecause there are 2 languages!')
    print(file.tell())
    d = file.tell() + 1
    file.write('\nСпасибо!')

    zz1 = [a, b, c, d]  # собрали в список данные по байтам начала строк
    zz3 = [1, 2, 3, 4]  # список нумерации строк
    pz = (dict(zip(zz3, zz1)))

    for i in pz.items():
        for j in string:
            print(dict(zip([i], [j])))

    file.close()


custom_write('dzposicion.txt', info)
