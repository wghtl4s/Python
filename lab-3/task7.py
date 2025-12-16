def zavdannya_7():
    
    while True:
        text = input("Введіть текст англійською: ")
        if text.strip():
            break
        print("Помилка")

    words_list = text.split()
    proper_nouns = []
    punctuation = '.,!?;:()-"\n\r'
    
    for i, word_with_punct in enumerate(words_list):
        cleaned_word = word_with_punct.strip(punctuation)
        
        if not cleaned_word or not cleaned_word.isalpha():
            continue
        if i > 0 and cleaned_word[0].isupper() and len(cleaned_word) > 1:
            if not cleaned_word.isupper():
                 proper_nouns.append(cleaned_word)

    unique_nouns = sorted(list(set(proper_nouns)))
    
    print(f"\nСписок імен та власних назв (слова з великої літери всередині тексту): {unique_nouns}")
zavdannya_7()