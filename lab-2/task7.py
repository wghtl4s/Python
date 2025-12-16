
a = int(input("введіть початкове число a (0 <= a <= 50): "))

sum_of_squares = 0

for number in range(a, 51):
    sum_of_squares += number ** 2

print(sum_of_squares)   