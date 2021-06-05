from re import findall, IGNORECASE
expression = "[a-zA-Z']+[a-zA-Z]+'*|[a-zA-Z]"


def sort_words_by_count(words):
    result = {}

    for word in words:
        if word not in result:
            result[word] = words.count(word)

    return result

def top_3_words(text):
    words = [word.lower() for word in findall(expression, text, IGNORECASE)]
    sorted_words = sorted(sort_words_by_count(words).items(), key=lambda x: -x[1])

    return [sorted_words[i][0] for i in range(3)] if len(sorted_words) > 2 \
        else [word[0] for word in sorted_words]


tests = [
    "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e", # should return ["e", "ddd", "aa"]
    "  //wont won't won't",     # should return ["won't", "wont"]
    "  ...  ",                  # should return []
    "  '  ",                    # should return []
]

for test in tests:
    print(top_3_words(test))