def validate_part_one(num):
    atleast_2 = False
    num_str = str(num)
    prev_d = None

    for d in num_str:
        curr_d = int(d)
        if prev_d:
            # digits don't decrease
            if curr_d < prev_d:
                return False
            # check for consecutive digits
            if curr_d == prev_d:
                atleast_2 = True
        prev_d = curr_d

    if not atleast_2:
        return False
    return True


def validate_part_two(num):
    num_str = str(num)
    prev_d = None
    consecutive_d = [1]

    for d in num_str:
        curr_d = int(d)
        if prev_d:
            # digits don't decrease
            if curr_d < prev_d:
                return False
            # count consecutive digits
            if curr_d == prev_d:
                consecutive_d[-1] += 1
            # restart consecutive digits count
            else:
                consecutive_d.append(1)
        prev_d = curr_d
    
    # need an occurence of exactly 2 consecutive digits in num
    if 2 not in consecutive_d:
        return False
    return True


# seq 402328 864247 | grep -P '^(?=1*2*3*4*5*6*7*8*9*$).*(.)\1' | wc -l
def part_one(min_num, max_num):
    count = 0
    for current_num in range(min_num+1, max_num):
        if validate_part_one(current_num):
            count += 1
    return count


# seq 246515 739105 | grep -P '^(?=1*2*3*4*5*6*7*8*9*$).*(.)(?<!(?=\1)..)\1(?!\1)' | wc -l
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
