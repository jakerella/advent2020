import sys
from helpers import read_data_file

print('\n************* Day 09 *************\n')

preamble = 25

def part1():
    msg = read_data_file(sys.argv[1], convert=int)
    
    for i in range(preamble, len(msg)):
        found = False
        for j in range(i-preamble, i):
            for k in range(i-preamble, i):
                if not msg[j] == msg[k] and (msg[j] + msg[k]) == msg[i]:
                    found = True
        if not found:
            print('Part 1: invalid sum at index', i, msg[i])

def part2():
    msg = read_data_file(sys.argv[1], convert=int)
    
    invalid = None
    for i in range(preamble, len(msg)):
        found = False
        for j in range(i-preamble, i):
            for k in range(i-preamble, i):
                if not msg[j] == msg[k] and (msg[j] + msg[k]) == msg[i]:
                    found = True
        if not found:
            invalid = i
            print('Part 2: invalid sum at index', i, msg[i])

    end = invalid-1
    while end:
        sum = 0
        smallest = 9999999999999
        largest = 0
        for i in range(end, -1, -1):
            sum += msg[i]
            if msg[i] > largest:
                largest = msg[i]
            elif msg[i] < smallest:
                smallest = msg[i]
            
            if sum == msg[invalid]:
                print('Contiguous set range:', smallest, largest, '... sum:', smallest + largest)
                return
            elif sum > msg[invalid]:
                end -= 1
                break

part1()
part2()
