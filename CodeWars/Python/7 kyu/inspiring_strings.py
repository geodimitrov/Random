def longest_word(string_of_words):
    return sorted(string_of_words.split(), key=lambda x: len(x))[-1]
