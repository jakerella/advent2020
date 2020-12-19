import sys
import re
from helpers import read_data_file

print('\n************* Day 19 *************\n')

lines = read_data_file(sys.argv[1])
rules = {}
messages = []
for line in lines:
    if re.match(r'^[ab]+$', line):
        messages.append(line)

    match = re.match(r'^(\d+): ([\d \|]+)$', line)
    if match != None:
        def parse_set(s):
            return list(map(int, s.split(' ')))
        rule_sets = list(map(parse_set, match.group(2).split(' | ')))
        rules[int(match.group(1))] = rule_sets
    
    match = re.match(r'^(\d+): "([ab])"$', line)
    if match != None:
        rules[int(match.group(1))] = match.group(2)
    
# print(rules)
# print(messages)

def process_rule_seq(seq):
    seq_patterns = ['']

    for index in seq:
        if type(rules[index]) is str:
            for i in range(len(seq_patterns)):
                seq_patterns[i] += rules[index]
        else:
            new_patterns = []
            for sub in rules[index]:
                sub_patterns = process_rule_seq(sub)
                for sub_p in sub_patterns:
                    for prev_p in seq_patterns:
                        new_patterns.append(prev_p + sub_p)
            seq_patterns = new_patterns
                
    return seq_patterns


def part1():
    patterns = process_rule_seq(rules[0][0])
    # print(patterns)
    count = 0
    for m in messages:
        if m in patterns:
            count += 1
    print('valid:', count)


def part2():
    rules[8] = [[42],[42,8]]
    rules[11] = [[42,31],[42,11,31]]

    rules_31 = process_rule_seq([31])
    rules_42 = process_rule_seq([42])
    # print('31', rules_31)
    # print('42', rules_42)

    def count_patterns(message, patterns):
        count = 0
        while True:
            match = False
            for p in patterns:
                if message.endswith(p):
                    match = True
                    break
            if not match:
                return count
            else:
                count += 1
                message = message[:(-1 * len(patterns[0]))]
                # print('truncated message to', message)

    count = 0
    for m in messages:
        # print('processing 31s on', m)
        count_31 = count_patterns(m, rules_31)
        # print('found', count_31)
        if count_31 == 0:
            continue
        m = m[:(-1 * len(rules_31[0])) * count_31]

        # print('processing 42s on', m)
        count_42 = count_patterns(m, rules_42)
        # print('found', count_42)
        # m = m[:(-1 * len(rules_42[0])) * count_42]
        # if len(m) == 0:
        #     count += 1
        if count_42 * len(rules_42[0]) == len(m) and count_42 > count_31:
            count += 1

    # 413 (high)
    print('valid:', count)


part1()
part2()
