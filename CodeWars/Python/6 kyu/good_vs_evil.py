def good_vs_evil(good, evil):
    good_worth = {
        0: 1, 1: 2, 2: 3, 3: 3, 4: 4, 5: 10
    }

    evil_worth = {
        0: 1, 1: 2, 2: 2, 3: 2, 4: 3, 5: 5, 6: 10
    }

    good_total_strength = sum(good_worth[i] * int(n) for i, n in enumerate(good.split()))
    evil_total_strength = sum(evil_worth[i] * int(n) for i, n in enumerate(evil.split()))


    if good_total_strength > evil_total_strength:
        return 'Battle Result: Good triumphs over Evil'
    elif good_total_strength < evil_total_strength:
