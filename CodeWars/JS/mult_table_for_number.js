function multiTable(number) {
    let result = []
    for (i = 1; i < 11; i++) {
        result.push(`${i} * ${number} = ${i * number}`)
    }

    return result.join('\n')
