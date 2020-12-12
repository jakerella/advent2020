import sys
from helpers import read_data_file

print('\n************* Day 12 *************\n')

lines = read_data_file(sys.argv[1])
moves = list(map(lambda l: [l[0], int(l[1:])], lines))

def go(action, amount, direction):
    if action == 'N' or (action == 'F' and direction == 0):
        return [0,amount]
    elif action == 'S' or (action == 'F' and direction == 180):
        return [0,amount*-1]
    elif action == 'E' or (action == 'F' and direction == 90):
        return [amount,0]
    elif action == 'W' or (action == 'F' and direction == 270):
        return [amount*-1,0]
    else:
        print('BAD ACTION for move', action, direction)


def rotate_ship(action, amount, direction):
    if action == 'L':
        direction -= amount
    elif action == 'R':
        direction += amount
    else:
        print('BAD ROTATION', action)

    if direction < 0:
        direction = 360 + direction
    if direction > 359:
        direction -= 360
    return direction

def rotate_waypoint(direction, amount, current):
    if amount == 180:
        return [current[0]*-1, current[1]*-1]
    elif (direction == 'R' and amount == 90) or (direction == 'L' and amount == 270):
        return [current[1],current[0]*-1]
    elif (direction == 'R' and amount == 270) or (direction == 'L' and amount == 90):
        return [current[1]*-1,current[0]]


def part1():
    loc = [0,0]   # [x,y]
    direction = 90

    for move in moves:
        if move[0] == 'L' or move[0] == 'R':
            direction = rotate_ship(move[0], move[1], direction)
            # print('rotated', move, 'to', direction)
        else:
            change = go(move[0], move[1], direction)
            loc[0] += change[0]
            loc[1] += change[1]
            # print('moved', move, direction, 'to', loc)

    print(loc, abs(loc[0]) + abs(loc[1]))


def part2():
    loc = [0,0]   # [x,y]
    waypoint = [10,1]   # [x,y]

    for move in moves:
        if move[0] == 'F':
            loc[0] += (waypoint[0] * move[1])
            loc[1] += (waypoint[1] * move[1])
            # print('moved ship', move, waypoint, 'to', loc)
        elif move[0] == 'L' or move[0] == 'R':
            waypoint = rotate_waypoint(move[0], move[1], waypoint)
            # print('rotated waypoint', move, 'to', waypoint)
        else:
            change = go(move[0], move[1], None)
            waypoint[0] += change[0]
            waypoint[1] += change[1]
            # print('moved waypoint', move, 'to', waypoint)

    print(loc, abs(loc[0]) + abs(loc[1]))
    

part1()
part2()
