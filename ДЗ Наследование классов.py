class Animal:  # животное

    def __init__(self, name, fed, alive):  #alive = True(живой) и fed = False(накормленный), name - индивидуальное
        self.alive = True
        self.fed = fed
        self.name = name
        self.ite_in()

    def ite_in(self):
        print(f'Меня зовут {self.name}, я люблю кушать {self.fed}.')

    def gad_octe1(self):
        print(f'{self.name}, для меня гадость бананы.')

    def gad_octe2(self):
        print(f'{self.name}, для меня гадость мясо.')

    def sit_iy(self):
        print(f'{self.name}, Когда я ем {self.fed} я сытый очень!')

    def sravn_nie1(self):
        print(f'Если волк съест фиалку =\n {self.alive}')
    def sravn_nie2(self):
        print(f'Если слон съест апельсин =\n {self.alive}')
class Plant:  # растения
    def __init__(self, name1, name2, alive):  # edible = False(съедобность), name - индивидуальное название каждого растения
        self.name1 = name1  # Индивидуальное название каждого растения
        self.name2 = name2
        self.alive = True
        edible = 1           # съедобнсть
    def eat_1(self, name1):
        print(f'{self.name1}')

    def eat_2(self, name2):
        print(f'{self.name2}')



class Mammal(Animal):  # Млекопитающие
    def __init__(self, name, fed, alive):  #alive - живой
        self.name = name
        self.fed = fed
        self.alive = True


class Predator(Animal):  # хищник
    def __init__(self, name, fed, alive):
        self.name = name
        self.fed = fed
        self.alive = False

        #def eat(self):
        #print()


class Flower(Plant):  # Цветок
    def __init__(self, name1, edible, alive):
        super().__init__(name1, edible, alive)
        self.edible = edible
        self.alive = alive

    def eat_1(self):
        print(f'{self.name1}, не съедобна для волка!')


class Fruit(Plant):  # фрукт
    def __init__(self, name2, edible, alive ):
        super().__init__(name2, edible, alive)
        self.edible = edible
        self.name2 = name2


    def eat_2(self):
        print(f'{self.name2}, полезный фрукт для Слона!')


elefant = Mammal('Слон', 'бананы', 'живой')
volk = Predator('Волк', 'мясо', 'живой')
flower = Flower('Фиалка', 'не съедобен', False)
fruit = Fruit('Апельсин', 'съедобен', True)
volk.ite_in()
volk.sit_iy()
volk.gad_octe1()
elefant.ite_in()
elefant.sit_iy()
elefant.gad_octe2()
flower.eat_1()
fruit.eat_2()
#print(flower.eat_1)
#print(fruit.eat_2)
volk.sravn_nie1()
elefant.sravn_nie2()

