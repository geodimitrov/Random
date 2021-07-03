import re
ZIPCODE_EX = '[A-Z]{2}\s[0-9]{5}'


def add_street_name_and_number(address, str_names, str_numbers):
    street_name_and_number = re.split(ZIPCODE_EX, address)[0]
    street_number = street_name_and_number.split()[0]
    street_name = street_name_and_number.split()[1:]
    str_names.append(' '.join(street_name))
    str_numbers.append(street_number)


def group_addresses_by_zipcode(addresses_data, zipcode):
    list_addresses = addresses_data.split(',')
    street_names = []
    street_numbers = []

    for address in list_addresses:
        address_zipcode = re.findall(ZIPCODE_EX, address)[0]

        if address_zipcode == zipcode:
            add_street_name_and_number(address, street_names, street_numbers)

    if not street_names:
        return f'{zipcode}:/'

    return f'{zipcode}:{",".join(street_names)}/{",".join(street_numbers)}'


tests = [
    # 'OH 43071',
    # 'NY 56432',
    # 'NY 5643',
    "AA 45522"
]

# addresses = '123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432'
addresses = '22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45522,10 Surta Alley Goodtown GG 30654'


for test in tests:
    print(group_addresses_by_zipcode(addresses, test))