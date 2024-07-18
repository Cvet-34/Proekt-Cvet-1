#print('Hello') # ASCII таблица с числовым значением символов для понимания компьютера
#print(ord('a'))  соответствует число в таблице 97
#print(ord('A')) соответствует число в таблице 65
#print(ord('h')) соответствует числу в табличе 104
#print(ord('e'))

# переводим из символов в значения
#a = 'hello'
#chars = []
#for i in a:
#    chars.append(ord(i))
#print(chars) #получаем [104, 101, 108, 108, 111]


#переводим обратно из чисел в символы
#a = 'hello'
#chars = []
#for i in a:
#    chars.append(ord(i))
#s = ''
#for i in chars:
#    s += chr(i)
#print(s) # получаем hello

#a = 'hello'
#chars = []
#for i in a:
#    chars.append(ord(i))
#s = ''
#    s += chr(i)
#print(s)

#for i in range(128): #содержит 128 основных символов часто используемых ASCII
#    print(chr(i))

#for i in range(1000, 1500): # большое пайтон берет из «Unicode». «Unicode» содержит примерно 2000000 символов.
#    print(chr(i))

print(hex(ord('h'))) # смотрим в байтак это как выглядит
bb = b'\x68'
print(type(bb)) # класс 'bytes'
print(bb.decode()) # переводим обратно из байтов в символ h.  получили'h'
#Кодеровка - это соответствие символа определенному числовому значению