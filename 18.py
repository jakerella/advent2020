import sys
import copy
from helpers import read_data_file

print('\n************* Day 18 *************\n')

formulas = read_data_file(sys.argv[1])

def eval_group(start, f):
    op = '+'
    group_total = 0
    # print('group', f[start:])
    i = start
    while i < len(f):
        # print('looking at index', i)
        if f[i] == '(':
            result = eval_group(i+1, f)
            # print('performing:', group_total, op, result[0])
            if op == '+':
                group_total += result[0]
            else:
                group_total *= result[0]
            if result[1] == None:
                break
            else:
                i = result[1]
        elif f[i] == ')':
            # print('end group', group_total, 'at index', i)
            return [group_total, i]
        elif f[i] == '+':
            op = '+'
        elif f[i] == '*':
            op = '*'
        else:
            # print('performing:', group_total, op, int(f[i]))
            if op == '+':
                group_total += int(f[i])
            else:
                group_total *= int(f[i])
        i += 1
    return [group_total, None]


def part1():
    total = 0
    for f in formulas:
        t = eval_group(0, f.replace(' ', ''))[0]
        print('line total:', t)
        total += t
        
    print('DONE:', total)
    

def part2():
    print(2)


part1()
part2()
