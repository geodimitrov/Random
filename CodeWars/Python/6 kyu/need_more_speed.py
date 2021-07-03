# Not allowed to use built in functions, slicing, etc.

def reverse_seq(seq):
    for i in range(len(seq) // 2):
        seq[i], seq[len(seq) - i - 1] = seq[len(seq) - i - 1], seq[i]
    return seq

print(reverse_seq([1,2,3,4,5]))