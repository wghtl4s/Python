def zavdannya_5():
    
    while True:
        text = input("Введіть текст англійською: ")
        if text.strip():
            break
        print("Помилка")

    while True:
        start_letter = input("Введіть літеру N (початок слова, 1 символ): ").upper()
        end_letter = input("Введіть літеру P (кінець слова, 1 символ): ").upper()

        if (len(start_letter) == 1 and 'A' <= start_letter <= 'Z') and \
           (len(end_letter) == 1 and 'A' <= end_letter <= 'Z'):
            break
        else:
            print("Помилка")

    words_list = text.split()
    starts_with_N = []
    ends_with_P = []
    punctuation = '.,!?;:()-"\n\r'

    for word_with_punct in words_list:
        cleaned_word = word_with_punct.strip(punctuation)
        
        if cleaned_word and cleaned_word.isalpha():
            word_upper = cleaned_word.upper()
            
            if word_upper.startswith(start_letter):
                starts_with_N.append(cleaned_word)
            
            if word_upper.endswith(end_letter):
                ends_with_P.append(cleaned_word)

    print(f"\nСлова, що починаються на '{start_letter}': {', '.join(starts_with_N) if starts_with_N else 'Не знайдено'}")
    print(f"Слова, що закінчуються на '{end_letter}': {', '.join(ends_with_P) if ends_with_P else 'Не знайдено'}")

zavdannya_5()