from datetime import date

class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        
        year, month, day = map(int, birth_date.split('-'))
        self.birth_date = date(year, month, day)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"
    
    
if __name__ == "__main__":
    person = Person("Шевченко", "Тарас", "1995-03-09", "Kobzar")
    
    print(f"Повне ім'я: {person.get_fullname()}")
    print(f"Вік: {person.get_age()}")
    print(f"Нікнейм: {person.nickname}")