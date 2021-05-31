# decode the urls
from urllib import parse


tests = [
    "http://www.google.bg/search?q=C%23",       # expected: http://www.google.bg/search?q=C#
    "https://mysite.com/show?n%40m3=p3%24h0",   # expected: https://mysite.com/show?n@m3=p3$h0
    "http://url-decoder.com/i%23de%25?id=23"    # expected: http://url-decoder.com/i#de%?id=23
]

for test in tests:
    print(parse.unquote(test))