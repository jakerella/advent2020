import sys
from  math import floor
from helpers import read_data_file

print('\n************* Day 05 *************\n')


# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.

def binary_slice(min, max, pattern, index=0):
    # print('slice called with', min, max)
    if min == max:
        return min
    if pattern[index] == 'F' or pattern[index] == 'L':
        # print('recurse after lower', pattern[index], min, min+floor((max-min) / 2))
        return binary_slice(min, min+floor((max-min) / 2), pattern, index+1)
    else:
        # print('recurse after upper', pattern[index], max-floor((max-min) / 2), max)
        return binary_slice(max-floor((max-min) / 2), max, pattern, index+1)

def part1():
    seats = read_data_file(sys.argv[1], method='char')
    seat_ids = []
    
    for seat in seats:
        row = seat[0:7]
        col = seat[7:10]
        # print(row, binary_slice(0, 127, row))
        # print(col, binary_slice(0, 7, col))
        seat_ids.append((binary_slice(0, 127, row) * 8) + binary_slice(0, 7, col))
    seat_ids.sort()
    return seat_ids

def part2():
    seat_ids = part1()
    hold_id = 0
    for sid in seat_ids:
        if sid > (hold_id + 1):
            print('found gap at', hold_id+1)
        hold_id = sid


print(part1().pop())
part2()