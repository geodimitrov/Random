def decode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in message:

        if char in alphabet:
            char_index = alphabet.index(char)
            new_char = alphabet[-(char_index % 26) - 1]
            result += new_char

        else:
            result += char

    return result 