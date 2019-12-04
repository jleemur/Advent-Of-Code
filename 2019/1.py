import sys
import math


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


def part_one(masses):
    total_fuel_req = 0
    for mass in masses:
        total_fuel_req += calculate_fuel(mass)

    return total_fuel_req


def part_two(masses):
    total_fuel_req = 0
    for mass in masses:
        fuel_req = mass  # init fuel_req > 0
        while fuel_req > 0:
            fuel_req = calculate_fuel(fuel_req)
            total_fuel_req += fuel_req

    return total_fuel_req


if __name__ == '__main__':
    data = [int(l.strip()) for l in sys.stdin.readlines()]
    print(f"1. {part_one(data)}")
    print(f"2. {part_two(data)}")
