def title_case(title, minor_words=''):
    if not title:
        return ''

    title = title.lower().split()
    first_word = title[0].title()

    if len(title) > 1:
        first_word += ' '

    return first_word + ' '.join([w.title() if w not in minor_words.lower().split() else w for w in title[1:]])
