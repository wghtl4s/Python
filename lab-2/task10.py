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