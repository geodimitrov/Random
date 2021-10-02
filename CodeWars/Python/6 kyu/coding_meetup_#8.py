REGIONS = (
    'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'
)

def all_continents(lst):
    devs_regions = [el['continent'] for el in lst]
    return all(False for reg in REGIONS if reg not in devs_regions)