import sys
from helpers import read_data_file

print('\n************* Day 08 *************\n')


def run(instr):
    acc = 0
    called = []

    loc = 0
    while True:
        if loc in called:
            print('Already called loc', loc, acc)
            break
        if loc == len(instr):
            print('** Reached end of program:', acc)
            break
        if loc > len(instr) or loc < 0:
            print('Bad program (out of range)', loc, acc)
            break

        called.append(loc)

        if instr[loc][0] == 'nop':
            loc += 1
            continue
        elif instr[loc][0] == 'acc':
            acc += instr[loc][1]
            loc += 1
            continue
        elif instr[loc][0] == 'jmp':
            loc += instr[loc][1]
            continue


def part1():
    instr = read_data_file(sys.argv[1], splitStr=' ', convert=[str, int])
    
    run(instr)


def part2():
    instr = read_data_file(sys.argv[1], splitStr=' ', convert=[str, int])
    switchers = []

    for loc in range(len(instr)):
        if instr[loc][0] == 'nop' or instr[loc][0] == 'jmp':
            switchers.append(loc)
    
    for loc in switchers:
        switched = instr[:]
        if switched[loc] == 'nop':
            switched[loc] = ['jmp', switched[loc][1]]
        else:
            switched[loc] = ['nop', switched[loc][1]]
        # print('trying', switched)
        run(switched)


part1()
part2()
