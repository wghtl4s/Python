def zavdannya_2():
    
    while True:
        try:
            n = int(input("Введіть кількість елементів N: "))
            if n > 0:
                break
            print("N має бути додатнім числом.")
        except ValueError:
            print("Помилка: Введіть ціле число.")

    list_a = []
    for i in range(n):
        while True:
            try:
                element = int(input(f"Введіть елемент {i + 1}: "))
                list_a.append(element)
                break
            except ValueError:
                print("Помилка: Введіть ціле число.")

    list_b_positive = []
    list_c_other = []

    for item in list_a:
        if item > 0:
            list_b_positive.append(item)
        else:
            list_c_other.append(item)

    print(f"\nПочатковий список: {list_a}")
    print(f"Список B (додатні елементи): {list_b_positive}")
    print(f"Список C (інші елементи): {list_c_other}")

zavdannya_2()