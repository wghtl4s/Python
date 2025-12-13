import random

def zavdannya_6():
    
    LIST_SIZE = 10
    my_list = [random.randint(-50, 50) for _ in range(LIST_SIZE)]
    
    max_element = max(my_list)
    second_list = []

    for item in my_list:
        if item < max_element:
            square = item ** 2
            second_list.append(square)

    second_list.sort(reverse=True)

    print(f"\nВихідний список: {my_list}")
    print(f"Максимальний елемент: {max_element}")
    print(f"Квадрати менших чисел (за зменшенням): {second_list}")

zavdannya_6()