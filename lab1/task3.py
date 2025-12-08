import math 
try:
    a_str = input(" перше число (a): ")
    b_str = input(" друге число (b): ")
    c_str = input(" третє число (c): ")
    d_str = input(" четверте число (d): ")

    a = float(a_str)
    b = float(b_str)
    c = float(c_str)
    d = float(d_str)

    print(f" a={a}, b={b}, c={c}, d={d}")
    
    results = []
    
    results.append(a + b)  
    results.append(a - b)  
    results.append(a * b)  

    if b != 0:
        results.append(a / b)
    else:
        results.append(0.0) 

    results.append(a ** c) 
    
    if int(c) != 0:
        results.append(int(b) // int(c)) 
        results.append(int(b) % int(c))
   
    print(f"results: {results}")

    list_len = len(results)
    print(f"Кількість елементів: {list_len}")

    print("парні елементи (значення):")
    for num in results:
        if num % 2 == 0: 
            print(num)
except ValueError:
    print(" нечислове значення.")