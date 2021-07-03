class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__


def declare_winner(fighter1, fighter2, first_attacker):
    attacker, defender = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)

    while True:
        defender.health -= attacker.damage_per_attack

        if defender.health <= 0:
            return attacker.name

        attacker, defender = defender, attacker



tests = [
    (Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"),
    (Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry")
]

for test in tests:
    print(declare_winner(test[0], test[1], test[2]))
