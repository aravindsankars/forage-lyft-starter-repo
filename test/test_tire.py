import unittest

from tire import Carrigan, Octoprime

class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        wear = [0.1, 0.2, 0.3, 0.95]
        tire = Carrigan(wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear = [0.1, 0.2, 0.3, 0.5]
        tire = Carrigan(wear)
        self.assertTrue(tire.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        wear = [1.2, 0.8, 0.6, 0.5]
        tire = Octoprime(wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear = [0.7, 0.8, 0.6, 0.5]
        tire = Octoprime(wear)
        self.assertTrue(tire.needs_service())

if __name__ == '__main__':
    unittest.main()