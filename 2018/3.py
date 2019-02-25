import sys

overlap = {}

# part one: how many claims overlap
def part_one(claims):
    count = 0
    for c in claims:
        id, right, down, wide, tall = c[0], c[1], c[2], c[3], c[4]
        
        for x in range(right, wide+right):
            for y in range(down, tall+down):
                try:
                    overlap[x][y].append(id)
                    if len(overlap[x][y]) is 2:
                        count += 1
                except KeyError:
                    if x in overlap:
                        overlap[x].update({y: [id]})
                    else:
                        overlap[x] = {y: [id]}
    return count


# part_one() needs to be executed first
# part two: find claim id that doesn't overlap
def part_two(claims):
    num = int(claims[len(claims)-1][0])  # total number of ids
    ids = [i for i in range(1, num+1)]

    for x in overlap.keys():
        keys = overlap[x].keys()
        for y in keys:
            val = overlap[x][y]
            if len(val) > 1:
                for i in range(0, len(val)):
                    try:
                        ids.remove(int(val[i]))
                    except ValueError:
                        continue
    return ids[0]


# input:
# #1 @ 1,3: 4x5
# id @ 1 right, 2 down: 4 wide, 5 tall
if __name__ == '__main__':
    data = []

    for line in sys.stdin.readlines():
        line = line.strip().split()
        # construct a claim
        claim = []  # = [id, right, down, wide, tall]
        claim.append(line[0][1:])  # id
        position = line[2].split(',')
        claim.append(int(position[0]))  # right
        claim.append(int(position[1][:-1]))  # down
        dimension = line[3].split('x')
        claim.append(int(dimension[0]))  # wide
        claim.append(int(dimension[1]))  # top
        data.append(claim)

    print(part_one(data))
    print(part_two(data))
