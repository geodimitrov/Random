def initialize_names(name):
    names = name.split()
    names[1:-1] = [el[0] + '.' for el in names[1:-1]]
    return ' '.join(names)