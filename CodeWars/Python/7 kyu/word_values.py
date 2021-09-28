from string import ascii_lowercase


def name_value(my_list):
    alphabet = ascii_lowercase

    def get_str_value(strng):
        return sum(alphabet.index(x) + 1 for x in strng if x in alphabet)

    return [get_str_value(my_list[i]) * (i + 1) for i in range(len(my_list))]