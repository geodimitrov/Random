def get_dice_score(dice):
    result = {}

    for el in dice:
        if el not in result:
            result[el] = dice.count(el)

    return result


def calc_score(dice):
    total_score = 0
    dice_scores = get_dice_score(dice)

    for key, value in dice_scores.items():
        if key == 1:
            if value >= 3:
                total_score += (value - 3) * 100 + 1000
            else:
                total_score += value * 100

        elif key == 5:
            if value >= 3:
                total_score += (value - 3) * 50 + 500
            else:
                total_score += value * 50

        else:
            if value >= 3:
                total_score += key * 100

    return total_score


tests = [
    [2, 3, 4, 6, 2],    # should return 0
    [4, 4, 4, 3, 3],    # should return 400
    [2, 4, 4, 5, 4],    # should return 450
    [5, 1, 3, 4, 1],    # should return 250
    [1, 1, 1, 3, 1],    # should return 1100
    [1, 1, 1, 1, 1],    # should return 1200
    [5, 5, 5, 5, 5],    # should return 600
]

for test in tests:
    print(calc_score(test))