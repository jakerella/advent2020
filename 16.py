import sys
import re
from helpers import read_data_file

print('\n************* Day 16 *************\n')

info = read_data_file(sys.argv[1])
rules = {}
mine = []
nearby = []

for line in info:
    match = re.match(r'^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$', line)
    if match:
        rules[match.group(1)] = [range(int(match.group(2)), int(match.group(3))+1), range(int(match.group(4)), int(match.group(5))+1)]
        # rules[match.group(1)] = [[int(match.group(2)), int(match.group(3))], [int(match.group(4)), int(match.group(5))]]
    match = re.match(r'^your ticket: ([\d,]+)$', line)
    if match:
        mine = list(map(int, match.group(1).split(',')))
    match = re.match(r'^([\d,]+)$', line)
    if match:
        nearby.append(list(map(int, match.group(1).split(','))))

# print(rules, '\n', mine, '\n', nearby)


def part1():
    invalid = []
    for ticket in nearby:
        for n in ticket:
            valid = False
            for rule in rules:
                if n in rules[rule][0] or n in rules[rule][1]:
                    valid = True
            if not valid:
                invalid.append(n)
    
    print(invalid, 'sum', sum(invalid))
    

def part2():
    positions = []
    for ticket in nearby:
        possible_fields = []
        ticket_valid = True
        
        for i in range(len(ticket)):
            valid_n = False
            n_fields = set()
            for field in rules:
                if ticket[i] in rules[field][0] or ticket[i] in rules[field][1]:
                    valid_n = True
                    n_fields.add(field)
            if not valid_n:
                ticket_valid = False
                break
            possible_fields.append(n_fields)

        if ticket_valid:
            # print('possible fields for ticket:', possible_fields)
            for i in range(len(possible_fields)):
                if i > len(positions)-1:
                    positions.append(possible_fields[i])
                else:
                    # print('adding to pos', i, positions[i], '=>', possible_fields[i])
                    positions[i] = positions[i].intersection(possible_fields[i])

    singles = set()
    has_multiples = True
    while has_multiples:
        has_multiples = False
        for i in range(len(positions)):
            if len(positions[i]) == 1:
                # print('found single!', positions[i])
                singles.add(next(iter(positions[i])))
            else:
                positions[i] = positions[i] - singles
                if len(positions[i]) > 1:
                    has_multiples = True

    #         positions[i] = positions[i] - singles
    #         if len(positions[i]) > 1:
    #             print('dang', positions[i])
    print(positions)
    
    product = 1
    for i in range(len(positions)):
        if next(iter(positions[i])).startswith('departure'):
            product *= mine[i]

    print(product)


part1()
part2()
