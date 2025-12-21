import unittest

class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, count):
        self.number_of_units += count

class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

class TestShop(unittest.TestCase):
    def setUp(self):
        self.store = Shop("Тест-Маг", "Продукти")

    def test_initialization(self):
        self.assertEqual(self.store.shop_name, "Тест-Маг")
        self.assertEqual(self.store.store_type, "Продукти")
        self.assertEqual(self.store.number_of_units, 0)

    def test_set_units(self):
        self.store.set_number_of_units(100)
        self.assertEqual(self.store.number_of_units, 100)

    def test_increment_units(self):
        self.store.set_number_of_units(50)
        self.store.increment_number_of_units(10)
        self.assertEqual(self.store.number_of_units, 60)

    def test_discount_inheritance(self):
        ds = Discount("Акція", "Одяг")
        self.assertEqual(ds.discount_products, [])
        self.assertEqual(ds.shop_name, "Акція")

if __name__ == "__main__":
    unittest.main()