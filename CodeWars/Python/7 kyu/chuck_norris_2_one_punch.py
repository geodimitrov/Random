def one_punch(item):
    return ''.join(char for char in ' '.join(sorted(item.split())) if char not in 'aeAE') \
        if isinstance(item, str) and item else 'Broken!'