def zavdannya_6():
    
    while True:
        text = input("Введіть текст англійською (до 100 слів): ")
        if text.strip():
            break
        print("Помилка: Текст не може бути порожнім.")

    vowels = "AEIOUY"
    count = 0
    text_upper = text.upper()

    for char in text_upper:
        if char in vowels:
            count += 1

    print(f"\nКількість голосних літер у тексті: {count}")

zavdannya_6()