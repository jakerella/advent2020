
print('\n************* Day 25 *************\n')

# data = [5764801, 17807724]  # test
data = [335121, 363891]  # input
divisor = 20201227


def transform(subject, loop=999999999999, target=None):
    value = 1
    for i in range(loop):
        value *= subject
        value = value % divisor
        if target and value == target:
            return (value, i+1)
    return (value, loop)


def part1():
    result = transform(7, target=data[0])
    print(f'found {data[0]} on loop {result[1]}')
    key = transform(data[1], loop=result[1])
    print(f'found key: {key[0]}')


def part2():
    print(2)


part1()
part2()
