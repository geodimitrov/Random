def sort_by_language(arr):
    return sorted(arr, key=lambda x: (x['language'], x['first_name']))