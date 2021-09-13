def find_missing_letter(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(len(chars) - 1):
        curr_char = chars[i]
        next_char = chars[i + 1]

        if not alphabet.index(curr_char) + 1 == alphabet.index(next_char):
            return alphabet[alphabet.index(curr_char) + 1]