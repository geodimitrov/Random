def calculate_years(principal, interest, tax, desired):
    years = 0

    while principal < desired:
        years += 1
        annual_interest = principal * interest * (1 - tax)
        principal += annual_interest

    return years