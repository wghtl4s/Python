import random

def zavdannya_8():
    data_list = [random.uniform(-100, 100) for _ in range(30)]
    
    grouped_lists = []
    for i in range(0, 30, 3):
        sublist = data_list[i:i + 3]
        
        sum_abs = abs(sublist[0]) + abs(sublist[1]) + abs(sublist[2])
        
        grouped_lists.append((sum_abs, sublist))

    grouped_lists.sort(key=lambda x: x[0])
    
    result_lists = [x[1] for x in grouped_lists]
    
    print("\nОтримані списки (відсортовані за зростанням суми модулів):")
    for sum_abs, sublist in grouped_lists:
        rounded_list = [round(x, 2) for x in sublist]
        rounded_sum = round(sum_abs, 2)
        print(f"Сума модулів: {rounded_sum}, Список: {rounded_list}")
zavdannya_8()