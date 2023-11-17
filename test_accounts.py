import unittest
from accounts import *

class test_accounts(unittest.TestCase):
    def setUp(self):
        self.a1 = Account("Jordan")
        self.a2 = SavingAccount("Jame")

    def tearDown(self):
        del self.a1
        del self.a2
    
    def test_init(self):
        self.assertEqual(self.a1.get_name(), "Jordan")
        self.assertAlmostEqual(self.a1.get_balance(), 0)

        self.assertEqual(self.a2.get_name(), "Jame")
        self.assertAlmostEqual(self.a2.get_balance(), 100)

    def test_deposit(self):
        self.a1.deposit(-20.50)
        self.a1.deposit(0)
        self.a1.deposit(40)
        self.a1.deposit(10.01)
        self.assertAlmostEqual(self.a1.get_balance(), 50.01)

        self.a2.deposit(-34.76)
        self.a2.deposit(0)
        self.a2.deposit(39)
        self.a2.deposit(1.01)
        self.assertAlmostEqual(self.a2.get_balance(), 140.01)

    def test_withdraw(self):
        self.a1.withdraw(10)
        self.a1.withdraw(-8.8)
        self.a1.deposit(100)
        self.a1.withdraw(0)
        self.a1.withdraw(7.3)
        self.a1.withdraw(10)
        self.assertAlmostEqual(self.a1.get_balance(), 82.7)

        self.a2.withdraw(10)
        self.a2.withdraw(-8.8)
        self.a2.deposit(40)
        self.a2.withdraw(10)
        self.a2.withdraw(0)
        self.a2.withdraw(8.8)
        self.assertAlmostEqual(self.a2.get_balance(), 121.2)

    def test_set_balance(self):
        self.a1.set_balance(-3.3)
        self.assertAlmostEqual(self.a1.get_balance(), 0)
        self.a1.set_balance(13.37)
        self.assertAlmostEqual(self.a1.get_balance(), 13.37)

        self.a2.set_balance(-3.3)
        self.assertAlmostEqual(self.a2.get_balance(), 100)
        self.a2.set_balance(13.37)
        self.assertAlmostEqual(self.a2.get_balance(), 100)
        self.a2.set_balance(190.87)
        self.assertAlmostEqual(self.a2.get_balance(), 190.87)

    def test_set_name(self):
        self.a1.set_name("John")
        self.assertEqual(self.a1.get_name(), "John")

        self.a2.set_name("Michael")
        self.assertEqual(self.a2.get_name(), "Michael")

if __name__ == '__main__':
    unittest.main()