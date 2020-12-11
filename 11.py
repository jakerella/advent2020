import sys
import copy
from helpers import read_data_file

print('\n************* Day 11 *************\n')

start_room = read_data_file(sys.argv[1], method='char')

def check_adj_seat(i, j, room, limit):
    if room[i][j] == '.':
        return '.'
    adj_ocupied = 0
    for adj_i in range(i-1,i+2):
        for adj_j in range(j-1,j+2):
            if adj_i == i and adj_j == j:
                continue
            elif adj_i in range(0,len(start_room)) and adj_j in range(0,len(start_room[0])) and room[adj_i][adj_j] == '#':
                adj_ocupied += 1
    if adj_ocupied == 0:
        return '#'
    elif adj_ocupied >= limit:
        return 'L'
    else:
        return room[i][j]

def check_seat_view(i, j, room, limit):
    if room[i][j] == '.':
        return '.'
    adj_ocupied = 0
    for adj_i in range(i-1,i+2):
        for adj_j in range(j-1,j+2):
            if adj_i == i and adj_j == j:
                continue
            elif adj_i in range(0,len(start_room)) and adj_j in range(0,len(start_room[0])):
                if check_direction(i, j, adj_i - i, adj_j - j, room):
                    adj_ocupied += 1
    if adj_ocupied == 0:
        return '#'
    elif adj_ocupied >= limit:
        return 'L'
    else:
        return room[i][j]

def check_direction(i, j, i_change, j_change, room):
    while True:
        i += i_change
        j += j_change
        if i in range(0, len(room)) and j in range(0, len(room[0])):
            if room[i][j] == '#':
                return True
            elif room[i][j] == 'L':
                return False
        else:
            return False

def check_all_seats(seat_check, limit):
    prev_room = copy.deepcopy(start_room)
    hold_occupied = 0
    while True:
        occupied = 0
        current_room = copy.deepcopy(prev_room)
        for i in range(len(prev_room)):
            for j in range(len(prev_room[0])):
                current_room[i][j] = seat_check(i, j, prev_room, limit)
                if current_room[i][j] == '#':
                    occupied += 1
        prev_room = current_room
        if occupied == hold_occupied:
            break
        else:
            hold_occupied = occupied
    print(hold_occupied)

def part1():
    check_all_seats(check_adj_seat, 4)

def part2():
    check_all_seats(check_seat_view, 5)
    

part1()
part2()
