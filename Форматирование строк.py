print('Привет, ' + str(14)  + 'мир!') # Котонация срок
print('Меня зовут %s' % 'Денис')
print('Меня зовут %s, мне %s' % ('Денис', 14))
print('Меня зовут %(name)s, мне %(year)s' % {'name':'Денис', 'year':14}) #  метод процентю нужно знать. хоть и устаревший часто бывает
print('Я учусь в {}{}'.format('Urban', '-universiti')) # новый способ # метод Формат format есть еще не везде
print('Я учусь в {0}{1}{0}'.format('Urban', '-universiti')) # новый способ
print('Я учусь в {title}{postficx}{title}'.format(title='Urban', postficx='-universiti')) # новый способ
print(f'{'Urban' * 2} Это лучший университет!') # f' ф строка. новый метод в пайтон.