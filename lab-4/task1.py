def zavdannya_1():
    
    while True:
        try:
            n = int(input("введіть кількість елементів N: "))
            if n > 0:
                break
            print("N не додатнім числом.")
        except ValueError:
            print("Помилка")

    my_list = []
    for i in range(n):
        while True:
            try:
                element = int(input(f"Введіть елемент {i + 1}: "))
                my_list.append(element)
                break
            except ValueError:
                print("Помилка")

    max_element = max(my_list)
    
    reversed_list = my_list[::-1]

    print(f"\nМаксимальний елемент: {max_element}")
    print(f"Список у зворотному порядку: {reversed_list}")

zavdannya_1()