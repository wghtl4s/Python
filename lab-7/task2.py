import csv
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

def modifier(filename):
    contacts = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = list(reader.fieldnames)
        for row in reader:
            p = Person(row['surname'], row['first_name'], row['birth_date'], row.get('nickname'))
            row['fullname'] = p.get_fullname()
            row['age'] = p.get_age()
            contacts.append(row)

    new_fieldnames = list(fieldnames)
    new_fieldnames.insert(new_fieldnames.index('first_name') + 1, 'fullname')
    new_fieldnames.append('age')

    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

if __name__ == "__main__":
    test_file = "contacts.csv"
    with open(test_file, 'w', encoding='utf-8', newline='') as f:
        f.write("surname,first_name,birth_date,nickname\n")
        f.write("Nischenko,Olga,1814-03-09,Nischeta\n")
        


    