def enumerate_elements(elements):
    return [f"{i}: {elements[i-1]}" for i in range(1, len(elements) + 1)]


print(enumerate_elements(["a", "b"]))