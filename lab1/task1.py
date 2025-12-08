print("Завдання 1: ")
try:
    
    a_str = input("Введіть перше число  ")
    b_str = input("Введіть друге число  ")
    c_str = input("Введіть третє число  ")
    d_str = input("Введіть четверте число  ")

    a = float(a_str)
    b = float(b_str)
    c = float(c_str)
    d = float(d_str)

    print(f"змінні: a={a}, b={b}, c={c}, d={d}")

except ValueError:
    print("невірний формат числа")
    exit()
    