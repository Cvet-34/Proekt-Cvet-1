import logging

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {self.speed}')

    def run(self):
        try:
            self.distance += self.speed * 2
            logging.info(f'run выполнено успешно {self.distance} += {self.speed * 2}')
            self.distance += self.speed * 2
        except TypeError as err:
            logging.error(f'дистанция, не верный тип данных', exc_info=True)
            return

    def walk(self):
        try:
            logging.info(f'walk выполнено успешно, {self.distance} += {self.speed}')
            self.distance += self.speed
        except ValueError as err:
            logging.error(f'Неверно! скорость не может быть отрицательной', exc_info=True)
            return

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='DZLog.log',
                        format='%(asctime)s | %(levelname)s | %(message)s', encoding='UTF-8')

    first = Runner('Вася', 10)
    second = Runner('Илья', 5)
    third = Runner('Арсен', 10)

    t = Tournament(-101, first, second)

    print(t.start())
    print(first.run())
    print(first.walk())
    print(second.run())
    print(second.walk())
    print(third.run())
    print(third.walk())

