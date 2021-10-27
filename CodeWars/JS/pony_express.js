// solution with for loop

function riders(stations) {
    var ridersNeeded = 1;
    var distance = 0;

    for (s of stations) {

        if (distance + s > 100) {
            ridersNeeded += 1;
            distance = 0;
        };
        
        distance += s;
    };

    return ridersNeeded;
  }

// solution with while loop

function riders(stations) {
    var ridersNeeded = 1;
    var distance = 0;

    while (stations.length > 0) {

        if (distance + stations[0] > 100) {
            ridersNeeded += 1;
            distance = 0;
        };
        
        distance += parseInt(stations.splice(0, 1));
    };

    return ridersNeeded;
