def pig_it(text):
    return ' '.join(el[1:] + el[0] + 'ay' if el not in '!?,.' else el for el in text.split())