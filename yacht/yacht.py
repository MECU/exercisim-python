# Score categories
# Change the values as you see fit
YACHT = 'Y'
ONES = '1'
TWOS = '2'
THREES = '3'
FOURS = '4'
FIVES = '5'
SIXES = '6'
FULL_HOUSE = 'F'
FOUR_OF_A_KIND = 'K'
LITTLE_STRAIGHT = 'L'
BIG_STRAIGHT = 'B'
CHOICE = 'C'


def score(dice: list, category: str) -> int:
    if category == YACHT:
        if dice[0] == dice[1] and dice[1] == dice[2] and dice[2] == dice[3] and dice[3] == dice[4]:
            return 50
        return 0

    if category == ONES:
        return dice.count(1)
    if category == TWOS:
        return dice.count(2) * 2
    if category == THREES:
        return dice.count(3) * 3
    if category == FOURS:
        return dice.count(4) * 4
    if category == FIVES:
        return dice.count(5) * 5
    if category == SIXES:
        return dice.count(6) * 6

    if category == CHOICE:
        return sum(dice)

    dice.sort()

    if category == BIG_STRAIGHT:
        if dice[0] == 2 and dice[1] == 3 and dice[2] == 4 and dice[3] == 5 and dice[4] == 6:
            return 30
        return 0

    if category == LITTLE_STRAIGHT:
        if dice[0] == 1 and dice[1] == 2 and dice[2] == 3 and dice[3] == 4 and dice[4] == 5:
            return 30
        return 0

    small_count = dice.count(dice[0])
    large_count = dice.count(dice[4])

    if category == FOUR_OF_A_KIND:
        if small_count >= 4:
            return dice[0] * 4
        if large_count >= 4:
            return dice[4] * 4
        return 0

    if category == FULL_HOUSE:
        if (small_count == 2 and large_count == 3) or (small_count == 3 and large_count == 2):
            return sum(dice)

    return 0
