###################
# Author: JLeemur #####################
# http://adventofcode.com/2017/day/2 ##
#######################################
import sys

# type(input) = [[int]]
# return int
def part1(input):
	checksum = 0

	for row in range(0, len(input)):
		highest = 0
		lowest = sys.maxsize
		for col in range(0, len(input[row])):
			curr = input[row][col]
			if curr > highest:
				highest = curr
			if curr < lowest:
				lowest = curr
		checksum += (highest - lowest)

	return checksum

# type(input) = [[int]]
# return int
def part2(input):
	sum = 0

	for row in range(0, len(input)):
		found = False
		possible = [input[row][0]]
		for col in range(1, len(input[row])):
			curr = input[row][col]
			for i in range(0, len(possible)):
				if curr % possible[i] == 0:
					found = True
					sum += curr/possible[i]
					break
				elif possible[i] % curr == 0:
					found = True
					sum += possible[i]/curr
					break
			if found == True:
				break
			else:
				possible.append(input[row][col])

	return int(sum)

if __name__ == '__main__':
	input = []
	for line in open('day2.input'):
		lineSplit = line.strip().split('\t')
		inputLine = []
		for item in lineSplit:
			inputLine.append(int(item))
		input.append(inputLine)
	print("Part 1: " + str(part1(input)))
	print("Part 2: " + str(part2(input)))
