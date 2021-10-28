
function generatePairs(n) {
    var result = [];

    for (x=0; x <= n; x++) {
        for (y=x; y <= n; y++) {
            result.push([x, y]);
        };
    };
    return result;
}
