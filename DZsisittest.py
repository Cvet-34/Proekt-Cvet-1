import unittest
from unittest import TestCase

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


tournament = Tournament(90, "Усэйн", "Андрей", "Ник")


# Тест кейс. Класс с набором тестов для программы.
class TournamentTest(TestCase):
# мегасетап происходит в самом начале и один раз перед каждым кейсом тестов

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

#производится перед каждым нашим тестированием, позволяет создавать переменную, с помощью которой мы можем что либо изменять
    def setUp(self):
        self.ysain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)

# Происходит после завершения всех тестов
    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"{key}: {result}")


    @unittest.skipIf(True, 'Тест в этом кейсе заморожен')
    def test_tournament_start_ysain_nick(self):
        tournament = Tournament(90, self.ysain, self.nik)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nik)
        self.all_results["ysain_nik"] = results


    @unittest.skip('Работа теста остановлена, забег отменен.')
    def test_tournament_start_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nik)
        self.all_results["andrey_nik"] = results

    @unittest.skipIf(False, 'Пропускаем')
    def test_tournament_start_ysain_andrey_nick(self):
        tournament = Tournament(90, self.ysain, self.andrey, self.nik)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nik)
        self.all_results["ysain_andrey_nik"] = results


if __name__ == "__main__":
    unittest.main()
