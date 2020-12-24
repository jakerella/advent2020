import sys
from copy import deepcopy
from helpers import read_data_file

print('\n************* Day 23 *************\n')

cups = read_data_file(sys.argv[1], method='char', convert=int)[0]
print('start:', cups)

def next_index(i, length):
    next_i = i + 1
    if next_i >= length:
        next_i = 0
    return next_i

def possible_dest(curr, turn):
    next_cup = curr - 1
    if next_cup < 1:
        next_cup = 9
    if not next_cup in turn:
        return possible_dest(next_cup, turn)
    return next_cup

def place_cup(index, cup, turn):
    if index >= len(cups):
        return place_cup(0, cup, turn)
    else:
        turn.insert(index, cup)
        return turn

def part1():
    turn = cups[:]
    curr = 0
    for move in range(100):
        # turn = turn[:]
        removed = []
        active = turn[curr]
        # removed.append(next_index(curr, len(turn)))
        removed.append(turn.pop(next_index(curr, len(turn))))
        removed.append(turn.pop(next_index(curr, len(turn))))
        removed.append(turn.pop(next_index(curr, len(turn))))
        # print('remove indices', removed)
        # removed = list(map(turn.pop, removed))
        dest = possible_dest(active, turn)
        # print(f'on move {move+1} active={active} dest={dest} and removed={removed}')
        turn = place_cup(turn.index(dest)+1, removed[0], turn)
        turn = place_cup(turn.index(removed[0])+1, removed[1], turn)
        turn = place_cup(turn.index(removed[1])+1, removed[2], turn)
        curr = turn.index(active) + 1
        if curr >= len(turn):
            curr = 0
        # print(f'After Move {move+1}: {turn}')
    print(turn)
    order = []
    i = turn.index(1) + 1
    while True:
        if i >= len(turn):
            i = 0
        if turn[i] == 1:
            break
        order.append(turn[i])
        i += 1
    print(''.join(list(map(str,order))))


def part2():
    print(2)


part1()
part2()
