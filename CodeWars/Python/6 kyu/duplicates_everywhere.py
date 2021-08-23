def remove_duplicate_ids(obj):
    elements = []
    new_dict = {}

    for key, value in dict(sorted(obj.items(), key=lambda x: -int(x[0]))).items():
        new_dict[key] = []

        for el in value:
            if el not in elements:
                elements.append(el)
                new_dict[key].append(el)

    return dict(sorted(new_dict.items(), key=lambda x: int(x[0])))