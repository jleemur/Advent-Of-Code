def part_one(wire1, wire2):    
    return wire1


def part_two(wire1, wire2):
    return wire2


if __name__ == '__main__':
    wire1 = [wire for wire in input().split(',')]
    wire2 = [wire for wire in input().split(',')]
    print(f"1. {part_one(wire1, wire2)}")
    print(f"2. {part_two(wire1, wire2)}")
