class NameLengthError(ValueError):
    pass

def check_name(name):
    if len(name) < 10:
        raise NameLengthError(f"Ім'я '{name}' занадто коротке")

if __name__ == "__main__":
    try:
        check_name("Еліна")
    except NameLengthError as e:
        print(f"Помилка: {e}")