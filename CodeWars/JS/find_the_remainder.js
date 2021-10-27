// Solution 1 - use Math max & min methods
function remainder1(a, b){
    let max_el = Math.max.apply(Math, [a, b]);
    let min_el = Math.min.apply(Math, [a, b]);
    return max_el % min_el;
}

// Solution 2 - compare a and b
function remainder2(a, b){
    if (a > b)
        return a % b;
    else
        return b % a;
