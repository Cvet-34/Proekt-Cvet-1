class House: # Создали класс House.
    def __init__(self, name, number_of_floors): # создали метод __init__ создали отребуты
        self.name = name    # self = указание на обект
        self.number_of_floors = number_of_floors

    def go_to(self):
        self.new_floor  = int(input('нажмите кнопку этажа для подъема ')) # пользователь задает № этажа
        if self.number_of_floors >= self.new_floor >= 1: # если № этажа в диапозоне от 1-30 то "Поехали"
            print('Поехали')
        elif self.number_of_floors <= self.new_floor or self.new_floor < 1: # если № этажа в диапозоне до 0 или больше 30 то "нет такого этажа"
            print('Такого этажа несуществует')

    def go_to1(self):
        for i in range(1, self.new_floor + 1): # Выводит в консоль этажи с 1 до указанного пользователем.
            print(i)



gk = House('ЖК Эльбрус', 30) # передали значения атрибутов
print(gk.name, gk.number_of_floors)
gk.go_to()   # Применили логику прописанную в функции для нашей переменной-объекта.
gk.go_to1()    # Применили логику прописанную в функции для нашей переменной-объекта.

