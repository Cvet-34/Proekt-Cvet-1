class Vehicle:  # Создали родительский класс
    def __init__(self, owner, __model, __engine_power, __color, __COLOR_VARIANTS):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = __COLOR_VARIANTS

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self): #Метод принт печатает результат при передаче данный и  из родительсткого класса Vehicle и из дочернего Sedan.
        print(f' Владелец: {self.owner}, \n Марка автомобиля: {self.__model}, \n Мощность двигателя: {self.__engine_power}, \n Цвет автомобиля: {self.__color}')

    def set_color(self): # метор работает через ввод цветов. red такой цвет уже у машины, green - проверяется посписку, любой другой нельзя покрасить
        new_color = input('Введите цвет для перекраски авто ')
        a = new_color
        print(a)
        if new_color == self.__color:
            print('Такой цвет сейчас у машины')
        for i in self.__COLOR_VARIANTS:
            if i == new_color:
                print('Перекрасить в этот цвет можно')
                break
        else:
            print('Перекрасить в этот цвет нельзя')

class Sedan(Vehicle): # Создали дочерний класс
    def __init__(self, __PASSENGERS_LIMIT, owner, __model, __engine_power, __color, __COLOR_VARIANTS):
        super().__init__(owner, __model, __engine_power, __color, __COLOR_VARIANTS)
        self.__PASSENGERS_LIMIT = 5


vehicle1 = Vehicle('Oleg', 'Toyota Mark II', 500,
                   'red', ['blue', 'green', 'black', 'white'])
sedan = Sedan(5, 'Cergey', 'Toyota Mark II', 500, 'black'
              , ['blue', 'green', 'black', 'white'])

vehicle1.print_info()
vehicle1.get_color()

vehicle1.set_color()
sedan.print_info()
