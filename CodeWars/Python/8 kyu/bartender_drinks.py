def get_drink_by_profession(param):
    values = {
        'jabroni': 'Patron Tequila',
        'school counselor': 'Anything with Alcohol',
        'programmer': 'Hipster Craft Beer',
        'bike gang member': 'Moonshine',
        'politician': 'Your tax dollars',
        'rapper': 'Cristal',
    }

    return values[param.lower()] if param.lower() in values else 'Beer'