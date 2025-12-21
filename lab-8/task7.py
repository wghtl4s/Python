class ToRoman:
    def convert(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

class FromRoman:
    def convert(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                int_val += roman[s[i]] - 2 * roman[s[i - 1]]
            else:
                int_val += roman[s[i]]
        return int_val

if __name__ == "__main__":
    print(f"1994 у римських: {ToRoman().convert(1994)}")
    print(f"MCMXCIV у десяткових: {FromRoman().convert('MCMXCIV')}")