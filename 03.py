import sys
from helpers import read_data_file

print('\n************* Day 03 *************\n')

def part1():
    mountain = read_data_file(sys.argv[1], method='char')
    trees = 0
    pos = [0,0]

    # print(mountain)

    while pos[0] < len(mountain):
        if (pos[1] > len(mountain[0])-1):
            pos[1] = pos[1] - len(mountain[1])
        # print('checking:', pos) #, mountain[pos[1]][pos[0]])
        if (mountain[pos[0]][pos[1]] == '#'):
            trees += 1
        pos[1] += 3
        pos[0] += 1

    print('Part 1:', trees)

def part2():
    mountain = read_data_file(sys.argv[1], method='char')
    slopes = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))    
    treeMultiplier = 1

    for slope in slopes:
        trees = 0
        pos = [0,0]

        while pos[0] < len(mountain):
            if (pos[1] > len(mountain[0])-1):
                pos[1] = pos[1] - len(mountain[1])
            # print('checking:', pos) #, mountain[pos[1]][pos[0]])
            if (mountain[pos[0]][pos[1]] == '#'):
                trees += 1
            pos[1] += slope[1]
            pos[0] += slope[0]
        treeMultiplier *= trees

    print('Part 2:', treeMultiplier)


part1()
part2()
