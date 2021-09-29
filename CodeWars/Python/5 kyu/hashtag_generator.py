def generate_hashtag(s):
    if not s:
        return False

    modified_s = '#' + ''.join(w.title() for w in s.split())
    return modified_s if len(modified_s) <= 140 else False