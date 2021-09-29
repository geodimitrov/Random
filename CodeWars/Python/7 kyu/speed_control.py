# explicit solution
def gps(s, x):
    if len(x) < 2:
        return 0

    distances = [x[i] - x[i - 1] for i in range(1, len(x))]
    speeds = [(3600 * d) / s for d in distances]
    return max(speeds)