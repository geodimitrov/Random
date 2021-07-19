# Explicit is better than implicit. REMEMBER?
def alphabet_position(text):
    positions = []

    for char in text.lower():
        if char.isalpha():
            positions.append(str(ord(char) - 96))

    return ' '.join(positions)