from math import ceil


def calculate_tip(amount, rating):
    ratings = {
        'terrible': 0,
        'poor': 0.05,
        'good': 0.1,
        'great': 0.15,
        'excellent': 0.2
    }

    if rating.lower() not in ratings:
        return 'Rating not recognised'

    return ceil(amount * ratings[rating.lower()])
