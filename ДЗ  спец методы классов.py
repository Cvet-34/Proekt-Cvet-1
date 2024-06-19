class House:

    def __init__(self, name, numberOfFloors):
        self.name = name
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self):
        self.floors = int(input('Введите номер этажа '))
        print(f'numberOfFloors {self.floors}')


dom = House ('Дом контор',0)
print(dom.name, dom.numberOfFloors)
dom.setNewNumberOfFloors()