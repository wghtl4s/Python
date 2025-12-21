class Dog:
    mammal = "ссавець"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} має вік {self.age}"

    def speak(self, sound):
        return f"{self.name} каже {sound}"

class Labrador(Dog):
    nature = "дружній"
    breed = "Лабрадор"
    
    def behavior(self):
        return f"{self.name} активно махає хвостом"

class Terrier(Dog):
    nature = "енергійний"
    breed = "Тер'єр"
    
    def behavior(self):
        return f"{self.name} швидко бігає"

class Pets:
    def __init__(self, dogs):
        self.dogs = dogs

if __name__ == "__main__":
    my_dogs = [Labrador("Болт", 3), Terrier("Рекс", 5), Dog("Джек", 2)]
    my_pets = Pets(my_dogs)
    for dog in my_pets.dogs:
        print(dog.description())