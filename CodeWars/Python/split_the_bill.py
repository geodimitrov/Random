def split_the_bill(dict):
    bill_per_person = sum([value for value in dict.values()]) / len(dict)

    for person, money_paid in dict.items():
        money_to_receive = round(money_paid - bill_per_person, 2)
        dict[person] = money_to_receive

    return dict


tests = [
    {'A': 20, 'B': 15, 'C': 10},
    {'A': 40, 'B': 25, 'X': 10}
]

for test in tests:
    print(split_the_bill(test))