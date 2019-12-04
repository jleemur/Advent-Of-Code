import copy
import itertools

def part_one(intcode_orig, noun=12, verb=2):
    intcode = copy.deepcopy(intcode_orig)  # do not modify original
    intcode[1] = noun
    intcode[2] = verb

    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        pos_val1 = intcode[i+1]
        pos_val2 = intcode[i+2]
        pos_out = intcode[i+3]

        if opcode is 1:  # add
            intcode[pos_out] = intcode[pos_val1] + intcode[pos_val2]
        elif opcode is 2:  # multiply
            intcode[pos_out] = intcode[pos_val1] * intcode[pos_val2]
        elif opcode is 99:  # halt
            return intcode[0]


def part_two(intcode):
    solution = 19690720

    for noun, verb in itertools.product(range(1, 100), range(1, 100)):
        if part_one(intcode, noun, verb) == solution:
            return 100 * noun + verb


if __name__ == '__main__':
    data = [int(i) for i in input().split(',')]
    print(f"1. {part_one(data)}")
    print(f"2. {part_two(data)}")
