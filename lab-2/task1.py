import random
import math

nums = [random.randint(0, 100) for _ in range(20)]
result1 = [num for num in nums if num <= 50]
print(f"Початкові: {nums}")
print(f"Результат: {result1}")



print("\nЗАВДАННЯ 5 ")
try:
    N = int(input("N (> 1): "))
    if N > 1:
        K = 0
        while 5**K <= N:
            K += 1
        print(f"Найменше K: {K} (5^{K} = {5**K})")
    else:
        print("N має бути > 1.")
except ValueError:
    print("Невірний ввід.")
    
    print("\nАВДАННЯ 6 ")
a = int(input("введіть початкове число a: "))
b = int(input("введіть кінцеве число b (b >= a): "))

current_number = a
total_sum = 0

while current_number <= b:
    total_sum += current_number
    current_number += 1

print(total_sum)

print("\nЗАВДАННЯ 7 ")
    
a = int(input("введіть початкове число a (0 <= a <= 50): "))

sum_of_squares = 0

for number in range(a, 51):
    sum_of_squares += number ** 2

print(sum_of_squares)   

print("\nАВДАННЯ 8 ")

N = int(input("введіть ціле число  "))

K = 0
power_of_5 = 1

while power_of_5 <= N:
    K += 1
    power_of_5 *= 5

print(K)
    
    
    
print("\nАВДАННЯ 9 ")
try:
    n = int(input("n: "))
    start_i = int(math.sqrt(n))
    for i in range(start_i, n + 2):
        current = i ** 2
        if current > n:
            print(f"Перше : {current}")
            break
except ValueError:
    print("еевірний ввід.")

print("\nЗАВДАННЯ 10 ")
try:
    n_seq = int(input("n (i^2 + 1): "))
    i = 0
    current = 1
    while current <= n_seq:
        i += 1
        current = i**2 + 1
    print(f"перше > n: {current}")
except ValueError:
    print("невірний ввід.")

print("\nЗАВДАННЯ 11 ")
try:
    D = int(input("День (D): "))
    M = int(input("Місяць (M): "))
    ZODIAC_DATES = {
        1: (19, "Козеріг", "Водолій"), 2: (18, "Водолій", "Риби"),
        3: (20, "Риби", "Овен"), 4: (19, "Овен", "Телець"),
        5: (20, "Телець", "Близнюки"), 6: (21, "Близнюки", "Рак"),
        7: (22, "Рак", "Лев"), 8: (22, "Лев", "Діва"),
        9: (22, "Діва", "Терези"), 10: (22, "Терези", "Скорпіон"),
        11: (22, "Скорпіон", "Стрілець"), 12: (21, "Стрілець", "Козеріг")
    }
    if 1 <= M <= 12 and 1 <= D <= 31:
        threshold, prev_sign, next_sign = ZODIAC_DATES[M]
        sign = prev_sign if D <= threshold else next_sign
        print(f"Знак Зодіаку: {sign}")
 
except ValueError:
    print("невірний ввід.")

print("\nЗАВДАННЯ 12 ")
try:
    unit_code = int(input("номер одиниці (1-5): "))
    mass_value = float(input("Маса: "))
    
    FACTORS = {1: 1.0, 2: 1e-6, 3: 1e-3, 4: 1000.0, 5: 100.0}
    
    if unit_code in FACTORS:
        mass_kg = mass_value * FACTORS[unit_code]
        print(f"Маса в кг: {mass_kg:.6f} кг")
    
except ValueError:
    print("невірний ввід.")