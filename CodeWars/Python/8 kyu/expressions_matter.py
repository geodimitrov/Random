def expression_matter(a, b, c):
    expressions = [
        a + b + c,
        a * b * c,
        a + b * c,
        a * b + c,
        (a + b) * c,
        a * (b + c),
    ]

    return max(exp for exp in expressions)