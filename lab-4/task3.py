
import random

def zavdannya_3():
    
    LIST_SIZE = 20
    my_list = [random.randint(-50, 50) for _ in range(LIST_SIZE)]

    sum_odd_indices = 0
    
    for i in range(1, LIST_SIZE, 2):
        sum_odd_indices += my_list[i]

    print(f"\nСформований список: {my_list}")
    print(f"Сума елементів з непарними індексами: {sum_odd_indices}")

zavdannya_3()