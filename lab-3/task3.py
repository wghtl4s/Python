def zavdannya_3():
    
    while True:
        text = input("Введіть довільний текст: ")
        if text.strip():
            break
        print("Помилка: Текст не може бути порожнім.")

    while True:
        target_word = input("Введіть слово для пошуку: ")
        if target_word.strip() and target_word.isalpha():
            break
        print("Помилка: Слово для пошуку має бути одним словом.")

    text_lower = text.lower()
    target_lower = target_word.lower()

    punctuation = '.,!?;:()-"\n\r'
    temp_text = text_lower
    
    for char in punctuation:
        temp_text = temp_text.replace(char, ' ')
    
    words = temp_text.split()
    
    count = 0
    for word in words:
        if word == target_lower:
            count += 1
    
    print(f"\nСлово '{target_word}' зустрічається у тексті: {count} разів")
zavdannya_3()