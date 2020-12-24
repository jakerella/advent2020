import sys
from copy import deepcopy
from helpers import read_data_file

print('\n************* Day 24 *************\n')

paths = read_data_file(sys.argv[1])


def get_position(path):
    pos = [0,0]
    i = 0
    while i < len(path):
        if path[i] == 'e':
            pos[0] += 1
        elif path[i] == 'w':
            pos[0] -= 1
        else:
            name = path[i] + path[i+1]
            if name == 'se':
                if pos[1] % 2 == 1:
                    pos[0] += 1
                pos[1] += 1
            elif name == 'sw':
                if pos[1] % 2 == 0:
                    pos[0] -= 1
                pos[1] += 1
            elif name == 'ne':
                if pos[1] % 2 == 1:
                    pos[0] += 1
                pos[1] -= 1
            elif name == 'nw':
                if pos[1] % 2 == 0:
                    pos[0] -= 1
                pos[1] -= 1
            i += 1
        i += 1
    return pos


def part1():
    tiles = {}
    count_black = 0
    for path in paths:
        pos = get_position(path)
        # print(f'path {path}\nis at: {pos}')
        loc = ','.join(list(map(str,pos)))
        if not loc in tiles or tiles[loc] == 'w':
            tiles[loc] = 'b'
            count_black += 1
        else:
            tiles[loc] = 'w'
            count_black -= 1
        
    print(f'Black tiles: {count_black}')
    # print(tiles)


def part2():
    print(2)


part1()  # 236 (low)
part2()
