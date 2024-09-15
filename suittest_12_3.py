import unittest
import DZsisittest


#Систиматизация тестов
DZsisittestST = unittest.TestSuite()

DZsisittestST.addTest(unittest.TestLoader().loadTestsFromTestCase(DZsisittest.TournamentTest)) # Добавили новый блок тестов
#которые создал другой программист


#Далее можем сконфигурировать по запуску. можно сделать отдельный файл runер и в него сохр., а мы создать отдельную переменную.
runner = unittest.TextTestRunner(verbosity=2)
runner.run(DZsisittestST)