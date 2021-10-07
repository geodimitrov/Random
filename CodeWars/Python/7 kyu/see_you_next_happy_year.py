def next_happy_year(year):
    
    while True:
        year += 1
        
        if len(set(str(year))) == len(str(year)):
