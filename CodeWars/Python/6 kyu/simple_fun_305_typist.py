def typist(string):

    if string[0].islower():
        tap_count = 1
    else:
        tap_count = 2

    for i in range(1, len(string)):
        current_char = string[i]
        previous_char = string[i-1]

        if (current_char.islower() and previous_char.islower()) or \
                (current_char.isupper() and previous_char.isupper()):
            tap_count += 1
        else:
            tap_count += 2

    return tap_count

