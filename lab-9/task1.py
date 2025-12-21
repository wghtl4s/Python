class Alphabet:
    def __init__(self, lang='Ua', letters=list("АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ")):
        self.lang = lang
        self.letters = letters

    def print_alphabet(self):
        print(f"Алфавіт ({self.lang}): {' '.join(self.letters)}")

    def letters_num(self):
        return len(self.letters)

    def is_ua_lang(self, text):
        ua_letters = set("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")
        text_letters = set(text.lower())
        return any(char in ua_letters for char in text_letters)

class EngAlphabet(Alphabet):
    _en_letters_num = 26

    def __init__(self):
        super().__init__('En', list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def is_en_letter(self, char):
        return char.upper() in self.letters

    def letters_num(self):
        return self._en_letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."

if __name__ == "__main__":
    eng = EngAlphabet()
    eng.print_alphabet()
    print(f"Кількість букв: {eng.letters_num()}")
    print(f"Чи є 'J' англійською буквою? {eng.is_en_letter('J')}")
    print(f"Чи містить текст 'Щ' українські літери? {eng.is_ua_lang('Щ')}")
    print(f"Приклад тексту: {eng.example()}")