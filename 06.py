import sys
import re
from helpers import read_data_file

print('\n************* Day 06 *************\n')


def get_answers():
    with open(sys.argv[1], encoding = 'utf-8') as f:
        data = []
        group = []
        for line in f:
            line = line.split('\n')[0]
            if line == '':
                data.append(group)
                group = []
            else:
                group.append(line)
        data.append(group)
    return data

def part1():
    groups = get_answers()

    total = 0
    for group in groups:
        total += len(''.join(set(''.join(group))))

    print(total)

def part2():
    groups = get_answers()
    total = 0

    for group in groups:
        # print(len(set(group[0]).intersection(*group[1:len(group)])))
        total += len(set(group[0]).intersection(*group[1:len(group)]))

    print(total)


part1()
part2()
