const areaOrPerimeter = function(l , w) {
    let result = null;

    if (l == w)
        result = l * w;
    
    else
        result = 2 * l + 2 * w;

    return result;
