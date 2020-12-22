import sys
from copy import deepcopy
from helpers import read_data_file

print('\n************* Day 20 *************\n')

lines = read_data_file(sys.argv[1])
tiles = {}
curr_id = None
tile_rows = []
for line in lines:
    if line.startswith('Tile'):
        if curr_id != None:
            tiles[curr_id] = tile_rows
        tile_rows = []
        curr_id = line[5:9]
    elif line.startswith('.') or line.startswith('#'):
        tile_rows.append(line)
tiles[curr_id] = tile_rows # catch last tile
# print(tiles)

edges = {}

def set_tile_edges(tile_id):
    left = ''
    right = ''
    for row in tiles[tile_id]:
        left += row[0]
        right += row[9]
    edges[tile_id] = [
        tiles[tile_id][0], # top
        right,             # right
        tiles[tile_id][9], # bottom
        left               # left
    ]

# initial edge setting
for tile_id in tiles.keys():
    set_tile_edges(tile_id)
# print(edges)


def remove_borders():
    new_tiles = {}
    for tile_id in tiles.keys():
        new_rows = []
        for i in range(1,len(tiles[tile_id])-1):
            new_rows.append(tiles[tile_id][i][1:9])
        new_tiles[tile_id] = new_rows
    return new_tiles

def find_corners():
    corners = []
    for tile_id in edges.keys():
        edge_match = 0
        for edge in edges[tile_id]:
            for other_id in edges.keys():
                if tile_id != other_id:
                    for other_edge in edges[other_id]:
                        if edge == other_edge or edge[::-1] == other_edge:
                            edge_match += 1
        # print('tile', tile_id, 'has', edge_match, 'matching edges')
        if edge_match < 3:
            corners.append(tile_id)
    return corners


def part1():
    product = 1
    corners = find_corners()
    for tid in corners:
        product *= int(tid)
    print('corners:', product, corners)


def print_tile(tile_id):
    print('\nTILE:', tile_id)
    for row in tiles[tile_id]:
        print(row)


def rotate_tile(tile_id, dir='L'):
    # print_tile(tile_id)
    side_len = len(tiles[tile_id])
    rotated_tile = [] + [''] * side_len
    for i in range(side_len):
        for j in range(side_len):
            if dir == 'L':
                rotated_tile[side_len-1-j] += tiles[tile_id][i][j]
            elif dir == 'R':
                rotated_tile[j] = tiles[tile_id][i][j] + rotated_tile[j]
    tiles[tile_id] = rotated_tile
    # print_tile(tile_id)
    set_tile_edges(tile_id)
    
    return rotated_tile

def flip_tile(tile_id):
    # print_tile(tile_id)
    tiles[tile_id] = list(map(lambda r: r[::-1], tiles[tile_id]))
    # print_tile(tile_id)
    set_tile_edges(tile_id)

def find_adjacent(tile_id):
    found = []
    for side in range(4):
        for other_id in edges.keys():
            if tile_id == other_id:
                continue
            for pos in range(4):
                if edges[tile_id][side] == edges[other_id][pos] or edges[tile_id][side] == edges[other_id][pos][::-1]:
                    found.append(other_id)
                    # print('match', tile_id, side, 'to', other_id, pos)
                    break
    return found

adjacent_map = {}
for tile_id in tiles.keys():
    adjacent_map[tile_id] = find_adjacent(tile_id)
    # print('adjacents for', tile_id, adjacent_map[tile_id])


def find_next_side(tile_id, opposite_tile_id):
    sides = adjacent_map[tile_id][:]
    try:
        sides.remove(opposite_tile_id)
    except:
        True
    if len(adjacent_map[sides[0]]) != 4:  # is it an edge tile?
        return sides[0]
    else:
        return sides[1]


def part2():
    corners = find_corners()
    # print(corners)

    used_tiles = set()
    rows = [[]]
    # find the top row
    curr = corners[0]  # just use the first corner for top left
    while True:
        rows[0].append(curr)
        used_tiles.add(curr)
        adjacent = adjacent_map[curr]
        if curr == corners[0]:
            curr = adjacent[1]
        elif len(adjacent) == 2: # opposite corner
            break
        else:
            curr = find_next_side(curr, rows[0][-2])
    # print(rows)

    # find left side
    curr = corners[0]  # just use the first corner for top left
    while True:
        adjacent = adjacent_map[curr]
        if curr == corners[0]:
            curr = adjacent[0]
        elif len(adjacent) == 2: # bottom corner
            break
        else:
            curr = find_next_side(curr, rows[-2])
        rows.append([curr])
        used_tiles.add(curr)
    print(rows)

    # fill it in
    for i in range(1, len(rows)):
        for j in range(1, len(rows[0])):
            tile = set(adjacent_map[rows[i-1][j]]).intersection(set(adjacent_map[rows[i][j-1]])).difference(used_tiles)
            rows[i].append(tile.pop())
    print(rows)

    # w00t... I have all the tiles... now I need to orient them (rotate and flip)
    # then I can hunt monsters

part1()
part2()
