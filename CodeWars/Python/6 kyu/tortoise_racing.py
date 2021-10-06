from math import floor

def race(v1, v2, g):
    if v1 >= v2:
        return None
    
    dist_per_hour = v2 - v1
    
    seconds = floor(g / dist_per_hour * 3600) % 60
    minutes = floor((g / dist_per_hour) * 60) % 60
    hours = g // (v2 - v1)
    
    return [hours, minutes, seconds]
