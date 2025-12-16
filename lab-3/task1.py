

import re

def zavdannya_1():


    while True:
        text = input("Введіть текст українською (до 1000 слів): ")
        if text.strip():
            break
        print("Помилка")

    while True:
        prefix = input("Введіть префікс (слово, з якого мають починатися слова): ")
        if prefix.strip() and prefix.isalpha(): 
            break
        print("Помилка")

    prefix_lower = prefix.lower()
    count = 0

    words_with_punct = text.split()
    
    punctuation = '.,!?;:()-"\n\r'

    for word_with_punct in words_with_punct:
        cleaned_word = word_with_punct.strip(punctuation)
        if not cleaned_word:
            continue
    
        word_lower = cleaned_word.lower()
        
        if word_lower.startswith(prefix_lower):
            count += 1

    print(f"\nКількість слів, що починаються з '{prefix}' (без врахування регістру): **{count}**")
    print("-" * 40)


zavdannya_1()