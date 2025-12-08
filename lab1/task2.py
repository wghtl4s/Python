results = []
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
    
    results.append(a + b)  
    results.append(a - b)  
    results.append(a * b)  

    results.append(a / b)  
    results.append(a ** c) 
    results.append(int(b) // int(c) if int(c) != 0 else float('inf')) 
    results.append(int(b) % int(c) if int(c) != 0 else float('nan')) 

    print("результати операцій ( results):")
    print(results)

except TypeError:
    print("помилка")
    exit()