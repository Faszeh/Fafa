def sort_string(input_str):
    symbols = []
    digits = []
    letters = []

    for char in input_str:
        if char.isspace():
            continue
        elif char.isdigit():
            digits.append(char)
        elif char.isalpha():
            letters.append(char)
        else:
            symbols.append(char)

    symbols_part = ''.join(symbols)
    digits_part = ''.join(sorted(digits))
    letters_part = ''.join(sorted(letters, key=lambda x: (x.lower(), x)))
    
    return symbols_part + digits_part + letters_part


# دریافت ورودی و نمایش خروجی
input_str = input()
output = sort_string(input_str)
print(output)
