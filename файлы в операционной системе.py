import os  # Тема файлы в операционной системе, для работы импортитуем OS.


print(os.getcwd()) # Получаем при запуске путь где находимся
                    # C:\PythonProject\pythonProjectФорматирование строк\модуль 7
print('Текущая дериктория:', os.getcwd()) #Текущая дериктория: C:\PythonProject\pythonProjectФорматирование строк\модуль 7


#os.mkdir('second') # метод из os mkdir для создания еще одного файла-папка-директория
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('Текущая дериктория:', os.getcwd()) #Текущая дериктория: #C:\PythonProject\pythonProjectФорматирование строк\модуль 7\second
#os.makedirs(r'third\fourth') # добавили папки third и fourth в second и в директ. модуль7
#print(os.listdir())  # видим только одну папку third

#for i in os.walk('.'):  # в этом случае видим '.' начальная директория second и далее структуру
    #print(i)
# В итоге видим:
# ('.', ['third'], [])
# ('.\\third', ['fourth'], [])
# ('.\\third\\fourth', [], [])

# способ как отфильтровать содержимое
os.chdir(r'C:\PythonProject\pythonProjectФорматирование строк\модуль 7')
print('Текущая дериктория:', os.getcwd())
print(os.listdir())  # в общем

file = [f for f in os.listdir() if os.path.isfile(f)]  # Для упорядоченного вывода файлов
dirs = [d for d in os.listdir() if os.path.isdir(d)]  # Для упорядоченного вывода директорий
#print(dirs)
#print(file)

os.startfile(file[0])  #в результате запустился текстовый документ sert.txt под индексом 0,
#print(os.stat(file[0])) # метод stat сведения о файле например: когда создан, когда открывлся, размер и др.
#print(os.stat(file[0]).st_size) # выводит текущий размер файла 26 байт
os.system('pip install random2') # можем передать что будем писать в командрой строке.? в результате запуска видим что такая зависимость уже установлена








