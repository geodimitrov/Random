def count_languages(lst):
    languages = [el['language']for el in lst]
    return {l: languages.count(l) for l in languages}