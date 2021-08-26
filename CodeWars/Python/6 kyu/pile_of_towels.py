def sort_the_pile(pile_of_towels, weekly_used_towels):

    for n in weekly_used_towels:
        basket = pile_of_towels[len(pile_of_towels) - n:]
        remaining_pile = pile_of_towels[:len(pile_of_towels) - n]
        pile_of_towels = remaining_pile + sorted(basket, reverse=True)

    return pile_of_towels