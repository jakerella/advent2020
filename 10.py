import sys
from helpers import read_data_file

print('\n************* Day 10 *************\n')

all_adapters = read_data_file(sys.argv[1], convert=int)
all_adapters.sort()

# print(all_adapters)

def find_smallest_next(current, adapters):
    next_index = 999999999
    next_num = 9999999999
    for i in range(len(adapters)):
        if adapters[i] - current < 4 and adapters[i] < next_num:
            next_num = adapters[i]
            next_index = i
    del adapters[next_index]
    return next_num

def part1():
    last_adapter = 0
    diffs = { 1: 0, 3: 0 }
    adapters = all_adapters[:]
    while len(adapters):
        next_num = find_smallest_next(last_adapter, adapters)
        diffs[next_num - last_adapter] += 1
        last_adapter = next_num
    
    diffs[3] += 1
    print(diffs[1] * diffs[3])


def find_paths(start, current_paths):
    if start == all_adapters[-1]:
        return 1

    if start in current_paths:
        return current_paths[start]

    paths = 0
    for i in range(1,4):
        if (start + i) in all_adapters:
            paths += find_paths(start + i, current_paths)  # recursively find paths for next step
    
    current_paths[start] = paths
    return paths

def part2():
    print(find_paths(0, {}))
    

part1()
part2()
