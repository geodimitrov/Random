def vowel_start(st):
    result = ''

    for char in st.lower():
        if char.isalnum and char in 'aeiou':
            result += ' ' + char
        elif char.isalnum():
            result += char

    return result.strip()