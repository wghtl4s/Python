try:
    unit_code = int(input("номер одиниці (1-5): "))
    mass_value = float(input("Маса: "))
    
    FACTORS = {1: 1.0, 2: 1e-6, 3: 1e-3, 4: 1000.0, 5: 100.0}
    
    if unit_code in FACTORS:
        mass_kg = mass_value * FACTORS[unit_code]
        print(f"Маса в кг: {mass_kg:.6f} кг")
    
except ValueError:
    print("невірний ввід.")