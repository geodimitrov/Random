function sumOfDifferences(arr) {
    arr = arr.sort((x, y) => y-x);
    let result = 0;

    for (i=0; i < arr.length - 1; i++)
        result += arr[i] - arr[i+1];

    return result;
