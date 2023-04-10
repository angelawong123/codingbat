def string_bits(str):
    """
    Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
    """
    result = ""
    for letter in range(0, len(str), 2):
        result += str[letter]
    return result

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))