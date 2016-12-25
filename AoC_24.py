###################
# Author: JLeemur #####################
# http://adventofcode.com/2016/day/24 #
#######################################

def main():
    grid = [] #input maze
    pos = [0,0] #current position
    with open('AoC_24_input.txt') as file: #open input file
        index = 0
        for line in file: #iterate through each line
            grid.append(line.replace('\n','')) #get rid of pesky '\n' at EOL
            if (line.find('0') != -1): #if 0 is in line, we want to save start pos
                pos[0] = index
                pos[1] = line.find('0')
            else:
                index += 1

    # We have starting position saved... how to find quickest route to find all nums??
    print grid[pos[0]][pos[1]]

if __name__ == '__main__':
    main()
