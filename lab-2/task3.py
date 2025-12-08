
import math


try:
    base = float(input("Основа (a): "))
    side = float(input("Бічна сторона (b): "))
    if base <= 0 or side <= 0 or base >= 2 * side:
        print("Трикутник не існує.")
    else:
        h = math.sqrt(side**2 - (base / 2)**2)
        area = 0.5 * base * h
        print(f"Площа: {area:.2f}")
        if area.is_integer() and int(area) % 2 == 0:
            print(f"Результат ділення на 2: {area / 2:.2f}")
except ValueError:
    print("Невірний ввід.")