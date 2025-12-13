import random

def zavdannya_7():
    
    my_list = [random.uniform(-100, 100) for _ in range(30)]
    
    min_abs_element = my_list[0]
    min_abs_value = abs(my_list[0])

    for item in my_list:
        current_abs = abs(item)
        if current_abs < min_abs_value:
            min_abs_value = current_abs
            min_abs_element = item

    my_list.sort()

    print(f"\nМінімальний по модулю елемент: {min_abs_element}")
    print(f"Відсортований список за збільшенням значення:")
    print([round(x, 2) for x in my_list])

zavdannya_7()