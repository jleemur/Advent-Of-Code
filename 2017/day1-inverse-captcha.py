###################
# Author: JLeemur #####################
# http://adventofcode.com/2017/day/1 ##
#######################################
# type(input) = str
# return int
def part1(input):
	length = len(input)
	sum = 0
	prev = int(input[0])

	for i in range(1,length):
		curr = int(input[i])
		if prev == curr:
			sum += curr
		prev = curr

	if int(input[0]) == int(input[length-1]):
		sum += int(input[0])

	return sum

# type(input) str
# return int
def part2(input):
	length = len(input)
	sum = 0
	steps = int(length/2)

	for i in range(0,length):
		curr = int(input[i])
		steps_index = (i+steps) % length
		steps_value = int(input[steps_index])

		if (curr == steps_value):
			sum += curr

	return sum

if __name__ == '__main__':
	for line in open('day1.input'):
		input = line.strip()
	print("Part 1: " + str(part1(input)))
	print("Part 2: " + str(part2(input)))
