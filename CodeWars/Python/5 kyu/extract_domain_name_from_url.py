values_to_remove = ('http://', 'https://', 'www.', 'http://www.', 'https://www.')


def domain_name(url):
    for value in values_to_remove:
        url = url.replace(value, '')

    return url.split('.')[0]
