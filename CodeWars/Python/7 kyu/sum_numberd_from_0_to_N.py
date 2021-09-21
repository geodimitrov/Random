def show_sequence(n):
    if n == 0:
        return '0=0'
    elif n < 0:
        return f'{n}<0'

    n_seq = '+'.join(str(i) for i in range(n + 1))
    n_seq_sum = sum(i for i in range(n + 1))

    return f'{n_seq} = {n_seq_sum}'