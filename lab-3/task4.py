import math
def zavdannya_4():
    
    while True:
        text = input("Введіть текст українською: ")
        if text.strip():
            break
        print("Помилка: Текст не може бути порожнім.")

    words_list = text.split()
    total_words = len(words_list)
    
    if total_words == 0:
        print("\nТекст не містить слів.")
        return

    half_index = math.ceil(total_words / 2)
    
    first_half = words_list[:half_index]
    second_half = words_list[half_index:]

    transformed_first_half = []
    for word in first_half:
        transformed_first_half.append(word.capitalize())
        
    transformed_second_half = []
    for word in second_half:
        transformed_second_half.append(word.lower() + " *")

    first_part = " ".join(transformed_first_half)
    second_part = " ".join(transformed_second_half)
    
    result_text = first_part + " | " + second_part.strip()

    print(f"\nПеретворений текст: {result_text}")

zavdannya_4()