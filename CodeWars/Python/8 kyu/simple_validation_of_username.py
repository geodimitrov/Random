allowed_chars = 'abcdefghijklmnopqrstuvwxyz1234567890_'


def validate_usr(username):
    result = [char for char in username if char not in allowed_chars]

    if not result and 3 < len(username) < 17:
        return True

    return False