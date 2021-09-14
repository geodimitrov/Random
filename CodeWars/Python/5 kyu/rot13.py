def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in message:
        if char.isalpha():
            char_index = alphabet.index(char.lower())
            new_char = alphabet[(char_index + 13) % len(alphabet)]

            if char.islower():
                result += new_char
            else:
                result += new_char.upper()

        else:
            result += char

    return result