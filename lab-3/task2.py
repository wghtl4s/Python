def zavdannya_2():
    
    while True:
        text = input("Введіть текст: ")
        if text.strip():
            break
        print("Помилка")

    replacement_count = text.count('а')
    new_text = text.replace('а', 'А')
    
    total_symbols = len(text)

    letter_count = 0
    for char in text:
        if char.isalpha():
            letter_count += 1

    print(f"\nОновлений текст: {new_text}")
    print(f"Кількість замін ('а' -> 'А'): {replacement_count}")
    print(f"Загальна кількість символів у рядку: {total_symbols}")
    print(f"Кількість літер у рядку: {letter_count}")
zavdannya_2()