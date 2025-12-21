class House:
    def __init__(self, area=100, price=50000):
        self.area = area
        self.price = price

    def final_price(self, discount):
        return self.price * (1 - discount / 100)

class SmallHouse(House):
    def __init__(self, price=20000):
        super().__init__(area=40, price=price)

class Human:
    default_name = "Elina"
    default_age = 19

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        house_info = self.__house.area if self.__house else "Відсутній"
        print(f"Ім'я: {self.name}, Вік: {self.age}, Гроші: {self.__money}, Будинок: {house_info} м2")

    @staticmethod
    def default_info():
        print(f"Стандартне ім'я: {Human.default_name}, Стандартний вік: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, discount=10):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            print("Будинок успішно куплено!")
        else:
            print("Попередження: Недостатньо коштів!")

if __name__ == "__main__":
    Human.default_info()
    person = Human("Олексій", 30)
    person.info()
    small_house = SmallHouse(15000)
    person.buy_house(small_house)
    person.earn_money(20000)
    person.buy_house(small_house)
    person.info()