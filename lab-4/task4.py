import random

def zavdannya_4():
    
    my_list = [random.randint(-100, 100) for _ in range(30)]

    max_element = my_list[0]
    max_index = 0
    
    for i in range(1, len(my_list)):
        if my_list[i] > max_element:
            max_element = my_list[i]
            max_index = i

    odd_list = []
    for item in my_list:
        if item % 2 != 0:
            odd_list.append(item)

    print(f"\nВихідний список: {my_list}")
    print(f"Максимальний елемент: {max_element}")
    print(f"Порядковий номер максимального елемента: {max_index + 1}")

    if odd_list:
        odd_list.sort(reverse=True)
        print(f"Список непарних чисел (за зменшенням): {odd_list}")
    else:
        print("Непарних чисел у списку немає.")

zavdannya_4()