class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Магазин: {self.shop_name}, Тип: {self.store_type}")

    def open_shop(self):
        print(f"Онлайн-магазин {self.shop_name} тепер відкритий!")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, count):
        self.number_of_units += count

class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discounts_products(self):
        print(f"Список товарів зі знижкою: {', '.join(self.discount_products)}")

if __name__ == "__main__":
    store = Shop("Glovo Market", "Продукти")
    print(f"Атрибут 1: {store.shop_name}")
    print(f"Атрибут 2: {store.store_type}")
    store.describe_shop()
    store.open_shop()

    # b
    shop1 = Shop("Comfy", "Електроніка")
    shop2 = Shop("Watsons", "Косметика")
    shop3 = Shop("Intertop", "Взуття")
    shop1.describe_shop()
    shop2.describe_shop()
    shop3.describe_shop()

    #  c, d
    print(f"Кількість видів товару: {store.number_of_units}")
    store.set_number_of_units(150)
    store.increment_number_of_units(25)
    print(f"Оновлена кількість: {store.number_of_units}")

    # e
    store_discount = Discount("Cyber Week", "Розпродаж")
    store_discount.discount_products = ["Смартфон", "Ноутбук", "Навушники"]
    store_discount.get_discounts_products()