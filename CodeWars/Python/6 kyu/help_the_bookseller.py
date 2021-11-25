# Explicit solution
def stock_list(books, categories):

    if not books or not categories:
        return ''

    result = []
    
    for cat in categories:
        total_stock_cat = sum(int(b.split()[1]) for b in books if b[0] == cat)
        result.append(f'({cat} : {total_stock_cat})')
    
