###################
# Author: JLeemur #####################
# http://adventofcode.com/2016/day/1  #
#######################################

#Returns compass direction after turn
def compass(direction, turn):
    if (direction == 'N' and turn == 'L') or (direction == 'S' and turn == 'R'):
        return 'W' #WEST
    elif (direction == 'N' and turn == 'R') or (direction == 'S' and turn == 'L'):
        return 'E' #EAST
    elif (direction == 'E' and turn == 'L') or (direction == 'W' and turn == 'R'):
        return 'N' #NORTH
    elif (direction == 'E' and turn == 'R') or (direction == 'W' and turn == 'L'):
        return 'S' #SOUTH

def main():
    file = open('AoC_1_input.txt', 'r')
    file_input = file.read().replace(',', '').split() #removes commas, then splits all input
    pointing = 'N' #default direction
    x = 0 #left and right: negative=west, positive=east
    y = 0 #up and down: negative=south, positive=north
    part2 = None
    path = [0,0]
    history = []

    #loop through all input
    for i in range(0,len(file_input)):
        pointing = compass(pointing, file_input[i][0])

        if (pointing == 'W'):
            x -= int(file_input[i][1:])
        elif (pointing == 'E'):
            x += int(file_input[i][1:])
        elif (pointing == 'N'):
            y += int(file_input[i][1:])
        elif (pointing == 'S'):
            y -= int(file_input[i][1:])

        if (part2 == None):
            if (path[0] < x):
                for n in range(path[0], x):
                    if [n,y] in history:
                        part2 = [n,y]
                        break
                    history.append([n,y])
            elif (path[0] > x):
                for n in range(path[0], x, -1):
                    if [n,y] in history:
                        part2 = [n,y]
                        break
                    history.append([n,y])
            elif (path[1] < y):
                for n in range(path[1], y):
                    if [x,n] in history:
                        part2 = [x,n]
                        break
                    history.append([x,n])
            if (path[1] > y):
                for n in range(path[1], y, -1):
                    if [x,n] in history:
                        part2 = [x,n]
                        break
                    history.append([x,n])

        path = [x,y] #set path to new coords

    print "Part 1: " + str(abs(x) + (abs(y)))
    print "Part 2: " + str(abs(part2[0]) + abs(part2[1]))


if __name__ == '__main__':
    main()
