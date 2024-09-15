import unittest
import DZsisittest


#Систиматизация тестов
DZsisittestST = unittest.TestSuite()

DZsisittestST.addTest(unittest.TestLoader().loadTestsFromTestCase(DZsisittest.TournamentTest)) # Добавили блок тестов



#Далее можем сконфигурировать по запуску.
runner = unittest.TextTestRunner(verbosity=2)
runner.run(DZsisittestST)