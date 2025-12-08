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
