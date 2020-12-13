import sys
from helpers import read_data_file

print('\n************* Day 13 *************\n')

lines = read_data_file(sys.argv[1])
delay = int(lines[0])
bus_ids = list(map(lambda x:int(x) if x.isdigit() else x, lines[1].split(',')))
print(delay, bus_ids)


def part1():
    next_bus = None
    wait_time = 0
    timestamp = delay
    while next_bus is None:
        for bus_id in filter(lambda x: type(x) is int, bus_ids):
            if timestamp % bus_id == 0:
                next_bus = bus_id
                wait_time = timestamp - delay
        timestamp += 1
    print('bus', next_bus, 'will be here in', wait_time, ':', next_bus * wait_time)


def part2():
    def get_bus(b):
        if b == 'x':
            return None
        return (b, bus_ids.index(b))
    bus_schedule = list(filter(lambda x: x != None, list(map(get_bus, bus_ids))))
    # print(bus_schedule)

    min_interval = bus_schedule[0][0]
    timestamp = 0

    for bus, index in bus_schedule[1:]:
        while True:
            if (timestamp + index) % bus == 0:
                min_interval = bus * min_interval
                break
            timestamp += min_interval

    print('start timestamp', timestamp)


part1()
part2()
