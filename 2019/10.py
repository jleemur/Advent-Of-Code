def validate_part_one(num):
    atleast_2 = False
    num_str = str(num)
    prev_d = None

    for d in num_str:
        curr_d = int(d)
        if prev_d:
            # left to right: the digits only increase / stay the same
            if curr_d < prev_d:
                return False
            # check for adjacent numbers
            if curr_d == prev_d:
                atleast_2 = True
        prev_d = curr_d

    if not atleast_2:
        return False
    return True


def validate_part_two(num):
    atleast_2 = False
    num_str = str(num)
    prev_d = None
    in_a_row_d = 1


    for d in enumerate(num_str):
        curr_d = int(d)
        if prev_d:
            # left to right: the digits only increase / stay the same
            if curr_d < prev_d:
                return False
            # check for adjacent numbers
            if curr_d == prev_d:
                atleast_2 = True
                in_a_row_d += 1
            else:
                if in_a_row_d > 2 and in_a_row_d % 2 is not 0:
                    return False
                in_a_row_d = 1
        prev_d = curr_d

    if not atleast_2:
        return False
    if in_a_row_d > 2 and in_a_row_d % 2 is not 0:
        return False
    print(num_str)
    return True


def part_one(min_num, max_num):
    count = 0
    for current_num in range(min_num+1, max_num):
        if validate_part_one(current_num):
            count += 1
    return count


def part_two(min_num, max_num):
    count = 0
    for current_num in range(min_num+1, max_num):
        if validate_part_two(current_num):
            count += 1
    return count


if __name__ == '__main__':
    data = [int(i) for i in input().split('-')]
    min_num = data[0]
    max_num = data[1]
    print(f"1. {part_one(min_num, max_num)}")
    print(f"2. {part_two(min_num, max_num)}")
