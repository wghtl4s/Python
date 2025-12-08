
try:
    amount = float(input("Сума покупки (грн): "))
    discount = 0
    if amount > 1000:
        discount = 0.05
    elif amount > 500:
        discount = 0.03
    final_cost = amount * (1 - discount)
    print(f"Знижка: {discount * 100}%")
    print(f"До сплати: {final_cost:.2f} грн")
except ValueError:
    print("Невірний ввід.")
