import sys

# part one:
## a) How many units remain after fully reacting the polymer you scanned?
def part_one(polymer):
    return polymer


def part_two(polymer):
    return polymer


# polymer:
## type is defined by letter
## polarity is defined by uppercase
## destroy adjacent characters with the same type & opposite polarity
## keep trying to react polymers until no more reactions exists
if __name__ == '__main__':
    polymer = input()
    print(part_one(polymer))
    print(part_two(polymer))
