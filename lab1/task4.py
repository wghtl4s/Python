try:
    print("введіть 5 чисел через пробіл.")
    user_input = input(" числа: ")
    
    results = []
    for item in user_input.split():
        results.append(float(item))

    if len(results) < 5:
        print(f"vи ввели лише {len(results)} чисел")
    else:
        print(f"список: {results}")

        results[1], results[4] = results[4], results[1]

        print(f"Змінений список:  {results}")

except ValueError:
    print("введено некоректні дані")