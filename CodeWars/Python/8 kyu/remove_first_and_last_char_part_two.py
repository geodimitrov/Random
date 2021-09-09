def array(string):
    result = string.replace(' ', '').split(',')
    return ' '.join(result[1:-1]) if len(result) > 2 else None


tests = [
        (''),       # should return None
        ('1'),      # should return None
        ('1, 3'),   # should return None
        ('1,2,3'),  # should return '2'
        ('1,2,3,4') # should return '2 3'
]

for test in tests:
    print(array(test))