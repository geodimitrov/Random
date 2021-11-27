def reverse_bits(n):
    n_to_binary_reversed = format(n, 'b')[::-1]
    return int(n_to_binary_reversed, 2)
