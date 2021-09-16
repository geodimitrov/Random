def solution(s):
    return ''.join(' ' + char if char.isupper() else char for char in s )