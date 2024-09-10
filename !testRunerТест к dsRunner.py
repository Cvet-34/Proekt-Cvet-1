
from unittest import TestCase

import dsRunner

import unittest


class RunnerTest(unittest.TestCase):
    def test_run(self):
        while dsRunner.runz.walk in range(10):
            self.assertEqual(dsRunner.runz.run(), 100)

    def test_walk(self):
        while dsRunner.runz1.walk in range(10):
            self.assertEqual(dsRunner.runz1.walk(), 50)

    def test_challenge(self):
        while dsRunner.runz.walk in range(10):
            self.assertEqual(dsRunner.runz.run(), 100)
        while dsRunner.runz1.walk in range(10):
            self.assertEqual(dsRunner.runz1.walk(), 50)
            self.assertNotEqual(dsRunner.runz1.walk() != dsRunner.runz.run()) # дистанции не равны

if __name__ == '__main__':
    unittest.main()
