import sys
import signal
from helpers import read_data_file

print('\n************* Day 15 *************\n')

starting = read_data_file(sys.argv[1], method='comma', convert=int)[0]


def find_last_spoken(top):
    try:
        spoken = {}
        for i in range(len(starting)):
            spoken[starting[i]] = [i]
        
        last = starting[-1]
        for turn in range(len(starting),top):
            # if not last in spoken:
            #     print('turn', turn, last, 'is new (0)')
            #     spoken[0] = [spoken[0][0],turn]
            #     last = 0
            # else:
            new = turn - 1 - spoken[last][0]
            # print('turn', turn, last, 'spoken at', spoken[last][0], 'setting', new)
            if new in spoken:
                spoken[new] = [spoken[new][-1], turn]
            else:
                spoken[new] = [turn]
            last = new
    except KeyboardInterrupt:
        print('turn:', turn)
        sys.exit()
    # print(spoken)
    print(last)


def part1():
    find_last_spoken(2020)

def part2():
    find_last_spoken(30000000)


part1()
part2()
