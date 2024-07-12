class Horse:  # Класс описывающий лошадь

    def __init__(self, x_distance, sound, y_distance):
        super().__init__(sound, y_distance)
        self.x_distance = x_distance  # пройденный путь
        self.y_distance = y_distance  # высота полёта
        self.sound = 'Frrr' # звук, который издаёт лошадь.

    def run(self):
        self.dx = 10
        print(self.x_distance + self.dx) # dx  изменение дистанции, увеличивает x_distance на dx.


class Eagle:  # Класс описывающей орла.
    def __init__(self, y_distance, sound):
        self.y_distance = y_distance  # высота полёта 'I train, eat, sleep, and repeat'
        self.sound = sound  # звук, который издаёт орёл(отсылка)

    def fly(self):
        self.dy = 15
        print(self.y_distance + self.dy) #где dy - изменение дистанции, увеличивает y_distance на dy.


class Pegasus(Horse, Eagle):  # класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
    # Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
    def __init__(self, x_distance, sound, y_distance):
        super().__init__(y_distance, sound, y_distance)
        self.x_distance = x_distance
        self.sound = sound
        self.fly()
        self.run()

    def move(self):  # где dx и dy изменения дистанции. В этом методе запускауеся
        print((self.dx, self.dy))  # наследованныем методы run и fly.

    def get_pos(self):  #возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же поря ке.
        print((self.x_distance, self.y_distance))

    def voice(self):  #который печатает значение унаследованного атрибута sound.
        print({self.sound})


print(Pegasus.mro())  # проверяем наслдование

p1 = Pegasus(0, 'I train, eat, sleep, and repeat', 0)

print(p1.get_pos())
p1.move()
print(p1.get_pos())
p1.voice()
