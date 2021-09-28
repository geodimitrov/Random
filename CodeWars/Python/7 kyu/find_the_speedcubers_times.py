def cube_times(times):
    avg_speed = round(sum(sorted(times)[1:-1]) / 3, 2)
    fastest_solve = min(times)
    return avg_speed, fastest_solve