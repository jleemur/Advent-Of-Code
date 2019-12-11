import copy


ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
HALT = 99


def part_one(intcode_in):
    intcode = copy.deepcopy(intcode_in)  # do not modify original

    # for i in range(0, len(intcode), 4):
    #     opcode = intcode[i]
    #     pos_val1 = intcode[i+1]
    #     pos_val2 = intcode[i+2]
    #     pos_output = intcode[i+3]

    #     if opcode is ADD:
    #         intcode[pos_output] = intcode[pos_val1] + intcode[pos_val2]
    #     elif opcode is MULTIPLY:
    #         intcode[pos_output] = intcode[pos_val1] * intcode[pos_val2]
    #     elif opcode is INPUT:
    #         pass
    #     elif opcode is OUTPUT:
    #         pass
    #     elif opcode is HALT:
    #         pass

    return intcode


def part_two(intcode_in):
    return 'tbd'


if __name__ == '__main__':
    data = [int(i) for i in input().split(',')]
    print(f"1. {part_one(data)}")
    print(f"2. {part_two(data)}")
