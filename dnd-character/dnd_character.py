import random
import math


class Character:
    abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

    def __init__(self):
        for attr in self.abilities:
            setattr(self, attr, self.setup_roll())

        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def setup_roll() -> int:
        rolls = [random.randint(1, 6) for _ in range(0, 4)]
        rolls.sort(reverse=True)
        rolls.pop(-1)

        return sum(rolls)

    def ability(self) -> int:
        return getattr(self, random.choice(self.abilities))


def modifier(value: int) -> int:
    return math.floor((value - 10) / 2)
