def ordered_count(inp):
    return list({char: inp.count(char) for char in inp}.items())



print(ordered_count("abracadabra"))