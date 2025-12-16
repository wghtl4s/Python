N = int(input("введіть ціле число  "))

K = 0
power_of_5 = 1

while power_of_5 <= N:
    K += 1
    power_of_5 *= 5

print(K)
    