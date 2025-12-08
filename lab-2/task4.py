
try:
    A = int(input("A (початок): "))
    B = int(input("B (кінець): "))
    total_sum = 0
    if A < B:
        for num in range(A, B + 1):
            total_sum += num
        print(f"Сума від {A} до {B}: {total_sum}")
    else:
        print("Умова A < B не виконується.")
except ValueError:
    print("Невірний ввід.")