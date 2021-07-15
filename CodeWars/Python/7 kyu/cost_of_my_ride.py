def insurance(age, size, num_of_days):
    car_sizes = {
        'economy': 0, 'medium': 10, 'full-size': 15
    }

    if num_of_days < 0:
        return 0

    total_cost = num_of_days * 50

    if age < 25:
        total_cost += num_of_days * 10

    if size in car_sizes:
        total_cost += num_of_days * car_sizes[size]
    else:
        total_cost += num_of_days * 15

    return total_cost