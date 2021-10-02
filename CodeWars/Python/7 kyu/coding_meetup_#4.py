def get_first_python(users):
    python_devs = [user for user in users if user['language'] == 'Python']

    if python_devs:
        return f'{python_devs[0]["first_name"]}, {python_devs[0]["country"]}'

    return 'There will be no Python developers'