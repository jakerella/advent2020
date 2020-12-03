import sys
from helpers import read_data_file

print('\n************* Day 02 *************\n')

def part1():
    passwords = list(map(formatEntry, read_data_file(sys.argv[1])))
    validCount = 0

    # print(passwords)

    for entry in passwords:
        count = entry['password'].count(entry['letter'])
        if (count in range(entry['min'], entry['max'] + 1)):
            validCount = validCount + 1

    print('Part 1:', validCount)

def part2():
    passwords = list(map(formatEntry, read_data_file(sys.argv[1])))
    validCount = 0

    # print(passwords)

    for entry in passwords:
        firstPos = entry['password'][entry['min'] - 1] == entry['letter']
        secondPos = entry['password'][entry['max'] - 1] == entry['letter']
        if ((firstPos and secondPos) or (not firstPos and not secondPos)):
            continue
        else:
            validCount = validCount + 1

    print('Part 2:', validCount)


def formatEntry(entry):
    pieces = entry.split(' ')
    counts = pieces[0].split('-')
    return { 'min': int(counts[0]), 'max': int(counts[1]), 'letter': pieces[1][0], 'password': pieces[2] }


part1()
part2()
