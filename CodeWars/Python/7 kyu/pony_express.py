def riders(stations):
    riders_needed = 1
    distance = stations.pop(0)

    while stations:

        if distance + stations[0] > 100:
            riders_needed += 1
            distance = 0

        distance += stations.pop(0)

