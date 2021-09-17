def namelist(names):
    if len(names) < 3:
        return ' & '.join(el['name'] for el in names)
    else:
        return ', '.join(el['name'] for el in names[:len(names) - 1]) + f' & {names[-1]["name"]}'