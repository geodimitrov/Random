def capital(capitals): 
    result = []

    for el in capitals:

        country, capital = el.values()
        result.append(f'The capital of {country} is {capital}')
    
