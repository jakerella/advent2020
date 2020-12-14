import sys
import re
from helpers import read_data_file

print('\n************* Day 14 *************\n')

lines = read_data_file(sys.argv[1])


def apply_mask(mask, value):
    masked_value = []
    masked_value += ['0'] * 36
    for i in range(len(mask)-1, -1, -1):
        if mask[i] == 'X':
            masked_value[i] = value[i]
        else:
            masked_value[i] = mask[i]
    return int(''.join(masked_value), 2)

def part1():
    mask = 0
    values = {}
    for line in lines:
        if line[0:4] == 'mask':
            mask = line[7:]
            # print('new mask:', mask)
        else:
            entry = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
            if entry == None:
                print('bad line:', line)
            else:
                address = int(entry.group(1))
                bin_value = str(bin(int(entry.group(2))))[2:].rjust(36, '0')
                values[address] = apply_mask(mask, bin_value)
    value_sum = 0
    for address in values:
        value_sum += values[address]
    print('sum of values', value_sum)


def address_mask(mask, addr):
    masked_value = []
    masked_value += ['0'] * 36
    for i in range(len(mask)-1, -1, -1):
        if mask[i] == '0':
            masked_value[i] = addr[i]
        else:
            masked_value[i] = mask[i]
    return ''.join(masked_value)

def assign_floating_bits(address_mask, value, values={}):
    if not 'X' in address_mask:
        # print('No Xs found, adding', value, 'at', address_mask)
        values[address_mask] = value
        return

    assign_floating_bits(address_mask.replace('X', '0', 1), value, values)
    assign_floating_bits(address_mask.replace('X', '1', 1), value, values)

def part2():
    mask = 0
    values = {}
    for line in lines:
        if line[0:4] == 'mask':
            mask = line[7:]
            # print('new mask:', mask)
        else:
            entry = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
            if entry == None:
                print('bad line:', line)
            else:
                value = str(bin(int(entry.group(2)))[2:]).rjust(36, '0')
                bin_address = str(bin(int(entry.group(1)))[2:]).rjust(36, '0')
                address = address_mask(mask, bin_address)
                assign_floating_bits(address, value, values)
    
    # print(values)

    value_sum = 0
    for address in values:
        value_sum += int(values[address], 2)
    print('sum of values', value_sum)

part1()
# 3906032069663 (low)
# 3926790061594
part2()
