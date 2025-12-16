
import math
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