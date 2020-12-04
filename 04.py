import sys
import re
from helpers import read_data_file

print('\n************* Day 04 *************\n')

required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def check_passport(passport):
    for field in required:
        if not field in passport:
            return False

        if field == 'byr':
            if not year_check(passport[field], 1920, 2002): return False
        if field == 'iyr':
            if not year_check(passport[field], 2010, 2020): return False
        if field == 'eyr':
            if not year_check(passport[field], 2020, 2030): return False
        if field == 'hgt':
            match = re.match(r'^(\d+)(cm|in)$', passport[field])
            if not match: return False
            if match.group(2) == 'cm' and (int(match.group(1)) < 150 or int(match.group(1)) > 193): return False
            if match.group(2) == 'in' and (int(match.group(1)) < 59 or int(match.group(1)) > 76): return False
        if field == 'hcl' and not re.match(r'^#[0-9a-f]{6}$', passport[field]):
            return False
        if field == 'ecl' and not re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', passport[field]):
            return False
        if field == 'pid' and not re.match(r'^\d{9}$', passport[field]):
            return False

    return True

def year_check(field, min, max):
    year = 0
    try: year = int(field)
    except: return False
    if year < min or year > max: return False
    return True

def get_passports():
    with open(sys.argv[1], encoding = 'utf-8') as f:
        data = []
        current = {}
        for line in f:
            line = line.split('\n')[0]
            if line == '':
                data.append(current)
                current = {}
            else:
                fields = line.split(' ')
                for field in fields:
                    nameValue = field.split(':')
                    current[nameValue[0]] = nameValue[1]
        data.append(current)
    return data

def part1():
    passports = get_passports()
    validCount = 0

    # print('passports:', len(passports), passports)

    for passport in passports:
        valid = True
        for field in required:
            if not field in passport:
                valid = False
        if valid:
            validCount += 1

    print('Part 1:', validCount)


def part2():
    passports = get_passports()
    validCount = 0

    for passport in passports:
        if check_passport(passport):
            validCount += 1

    print('Part 2:', validCount)


part1()
part2()
