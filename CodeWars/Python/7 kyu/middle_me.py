def middle_me(N, X, Y):
    if not N % 2 == 0:
        return X
    return f'{N // 2 * Y}{X}{N // 2 * Y}'