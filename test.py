import unittest
import modules.ioet_test as ioet

class TestIoetModule(unittest.TestCase):

    def test_day(self):
        self.assertEqual(ioet.calculateSalary("TEST","MO","10:00-12:00",False), 30, "Should be $30 for salary")

    def test_weekend(self):
        self.assertEqual(ioet.calculateSalary("TEST","SU","01:00-03:00",False), 60, "Should be $60 for salary")

if __name__ == '__main__':
    unittest.main()