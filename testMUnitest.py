import unittest
from unittest import TestCase
from dzMUnitest import Runner, Tournament


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


    def test_tournament_start_usain_nick(self):
        tournament = Tournament(90, self.ysain, self.nik)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nik)
        self.all_results["usain_nick"] = results

    def test_tournament_start_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nik)
        self.all_results["andrey_nick"] = results

    def test_tournament_start_usain_andrey_nick(self):
        tournament = Tournament(90, self.ysain, self.andrey, self.nik)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nik)
        self.all_results["usain_andrey_nick"] = results


if __name__ == "__main__":
    unittest.main()



