def word_to_bin(word):
    return [bin(ord(char)).replace('b', '') for char in word]