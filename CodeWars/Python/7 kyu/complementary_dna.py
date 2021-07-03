symbol_pairs = {
    'A': 'T', 'T': 'A',
    'C': 'G', 'G': 'C',
}


def dna_strand(dna):
    complemented_dna = ''
    for symbol in dna:
        complemented_dna += symbol_pairs[symbol]

    return complemented_dna


tests = [
    "ATTGC",
    "GTAT",
]

for test in tests:
    print(dna_strand(test))