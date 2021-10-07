def triangle(row):
    color_conversion = {
        'BG': 'R', 'GB': 'R',
        'RG': 'B', 'GR': 'B',
        'BR': 'G', 'RB': 'G'
    }

    while len(row) > 1:
        new_row = ''

        for i in range(len(row) - 1):
            new_row += color_conversion.get(row[i] + row[i+1], row[i])
        
        row = new_row
    
    return row
