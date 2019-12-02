import sys

# sum of numbers
def part_one(numbers):
    return sum(numbers)

# find first value to repeat
def part_two(numbers):
    # could improve by performing 1 iteration
    # calculate shift (sum at end of iteration)
    # finding the first value to repeat (using mod and shift)
    numbers_seen = [0]
    sum = 0
    while True:
        for number in numbers:
            sum += number
            if sum in numbers_seen:
                return sum
            numbers_seen.append(sum)

if __name__ == '__main__':
    data = [int(l.strip()) for l in sys.stdin.readlines()]
    print(part_one(data))
    print(part_two(data))
