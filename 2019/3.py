from collections import Counter

def get_wire_coords(path):
    x, y = 0, 0
    wire_coords = set()
    for rule in path:
        if rule[0] == 'U':
            value = int(rule[1:])
            for new_y in range(y+1, y+value+1):
                wire_coords.add((x,new_y))
            y += value
        elif rule[0] == 'D':
            value = int(rule[1:])
            for new_y in range(y-1, y-value-1, -1):
                wire_coords.add((x,new_y))
            y -= value
        elif rule[0] == 'R':
            value = int(rule[1:])
            for new_x in range(x+1, x+value+1):
                wire_coords.add((new_x,y))
            x += value
        elif rule[0] == 'L':
            value = int(rule[1:])
            for new_x in range(x-1, x-value-1, -1):
                wire_coords.add((new_x,y))
            x -= value
    if (0,0) in wire_coords:
        wire_coords.remove((0,0))  # (0,0) doesn't count
    return wire_coords

def count_steps_for_crossing_coords(path, coords):
    x, y = 0, 0
    steps_for_wire_coords = {}
    total_steps = 0
    for rule in path:
        if len(coords) == len(steps_for_wire_coords.keys()):
            break

        if rule[0] == 'U':
            value = int(rule[1:])
            for new_y in range(y+1, y+value+1):
                total_steps += 1
                if (x, new_y) in coords:
                    steps_for_wire_coords[(x,new_y)] = total_steps
            y += value
        elif rule[0] == 'D':
            value = int(rule[1:])
            for new_y in range(y-1, y-value-1, -1):
                total_steps += 1
                if (x, new_y) in coords:
                    steps_for_wire_coords[(x,new_y)] = total_steps
            y -= value
        elif rule[0] == 'R':
            value = int(rule[1:])
            for new_x in range(x+1, x+value+1):
                total_steps += 1
                if (new_x, y) in coords:
                    steps_for_wire_coords[(new_x,y)] = total_steps
            x += value
        elif rule[0] == 'L':
            value = int(rule[1:])
            for new_x in range(x-1, x-value-1, -1):
                total_steps += 1
                if (new_x, y) in coords:
                    steps_for_wire_coords[(new_x,y)] = total_steps
            x -= value

    return steps_for_wire_coords

def part_one(wire1_path, wire2_path):
    wire1_coords = get_wire_coords(wire1_path)
    wire2_coords = get_wire_coords(wire2_path)

    # get crossing all crossing coordinates
    crossing_paths = set(tuple())
    for coord in wire1_coords:
        if coord in wire2_coords:
            crossing_paths.add(coord)
    crossing_paths = list(crossing_paths)

    # find shortest manhattan distance
    first_crossing_path = crossing_paths.pop(0)
    shortest_manhattan_dist = abs(first_crossing_path[0]) + abs(first_crossing_path[1])
    for coord in crossing_paths:
        manhattan_dist = abs(coord[0]) + abs(coord[1])
        if manhattan_dist < shortest_manhattan_dist:
            shortest_manhattan_dist = manhattan_dist

    return shortest_manhattan_dist


def part_two(wire1_path, wire2_path):
    wire1_coords = get_wire_coords(wire1_path)
    wire2_coords = get_wire_coords(wire2_path)

    # get crossing all crossing coordinates
    crossing_paths = set(tuple())
    for coord in wire1_coords:
        if coord in wire2_coords:
            crossing_paths.add(coord)
    crossing_paths = list(crossing_paths)

    # count steps for all crossing coordinates, per wire
    crossing_coords_steps_wire1 = count_steps_for_crossing_coords(wire1_path, crossing_paths)
    crossing_coords_steps_wire2 = count_steps_for_crossing_coords(wire2_path, crossing_paths)

    # find minimum amount of steps
    crossing_coords_steps_sum = dict(Counter(crossing_coords_steps_wire1) + Counter(crossing_coords_steps_wire2))
    minimum_steps = min(crossing_coords_steps_sum.values())

    return minimum_steps


if __name__ == '__main__':
    wire1_path = [path for path in input().split(',')]
    wire2_path = [path for path in input().split(',')]
    print(f"1. {part_one(wire1_path, wire2_path)}")
    print(f"2. {part_two(wire1_path, wire2_path)}")
