class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def get_speed(self):
        return self.speed

if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2022)
    for _ in range(5):
        my_car.accelerate()
        print(f"Прискорення: {my_car.get_speed()}")
    for _ in range(5):
        my_car.brake()
        print(f"Гальмування: {my_car.get_speed()}")