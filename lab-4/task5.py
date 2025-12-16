import random

def zavdannya_5():
    my_list = [random.randint(-100, 100) for _ in range(30)]
    
    negative_pairs = []

    for i in range(len(my_list) - 1):
        current = my_list[i]
        next_item = my_list[i + 1]
        
        if current < 0 and next_item < 0:
            negative_pairs.append((current, next_item))

    print(f"\nВихідний список: {my_list}")
    
    if negative_pairs:
        print("Пари від'ємних чисел, що стоять поруч:")
        for pair in negative_pairs:
            print(pair)
    else:
        print("Пари від'ємних чисел, що стоять поруч, не знайдено.")

zavdannya_5()