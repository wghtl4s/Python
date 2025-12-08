a = int(input("введіть початкове число a: "))
b = int(input("введіть кінцеве число b (b >= a): "))

current_number = a
total_sum = 0

while current_number <= b:
    total_sum += current_number
    current_number += 1

print(total_sum)