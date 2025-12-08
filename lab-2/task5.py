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