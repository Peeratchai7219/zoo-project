import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
    
    def test_child_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "error")

    def test_child_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_child_ticket_price3(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_child_ticket_price4(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_child_ticket_price5(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_child_ticket_price6(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_child_ticket_price7(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

        self.assertEqual(self.zoo.get_ticket_price(61), 100)
   

if __name__ == '__main__':
    unittest.main()
