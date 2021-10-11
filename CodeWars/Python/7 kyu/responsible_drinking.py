import re

def hydrate(drink_string): 
    water_glasses = sum(map(int, re.findall('\d+', drink_string)))

    if water_glasses == 1:
        return f'1 glass of water'
        
