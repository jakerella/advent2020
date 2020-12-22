import sys
from copy import deepcopy
from helpers import read_data_file

print('\n************* Day 21 *************\n')

products = read_data_file(sys.argv[1])
possile_allergens = {}
all_ingredients = set()
product_ingredients = []
for product in products:
    parts = product.split(' (contains ')
    ingredients = set(parts[0].split(' '))
    all_ingredients = all_ingredients.union(ingredients)
    product_ingredients.append(ingredients)
    for allergen in parts[1][0:-1].split(', '):
        if not allergen in possile_allergens:
            possile_allergens[allergen] = set(ingredients)
        else:
            possile_allergens[allergen] = possile_allergens[allergen].intersection(set(ingredients))

allergens_copy = deepcopy(possile_allergens)
def find_next_single():
    for allergen in allergens_copy:
        if len(allergens_copy[allergen]) == 1:
            return allergen
    return None

allergen_map = {}
while len(allergens_copy):
    single_allergen = find_next_single()
    if single_allergen == None:
        break
    allergen_map[single_allergen] = list(allergens_copy[single_allergen])[0]
    # print('determined that', single_allergen, 'is in', list(allergens_copy[single_allergen])[0])
    allergens_copy.pop(single_allergen)
    for allergen in allergens_copy:
        # print('removing', set([allergen_map[single_allergen]]), 'from', allergens_copy[allergen])
        allergens_copy[allergen] = allergens_copy[allergen].difference(set([allergen_map[single_allergen]]))
    # print('new possible allergens:', allergens_copy)

# print('possible allergens', possile_allergens)
# print('all ingredients', all_ingredients)
print('allergen map', allergen_map)


def part1():
    safe_ingredients = deepcopy(all_ingredients)
    for allergen in possile_allergens:
        safe_ingredients = safe_ingredients.difference(possile_allergens[allergen])
    print('safe ingredients', safe_ingredients)
    count = 0
    for ingredient in safe_ingredients:
        for ingredient_list in product_ingredients:
            if ingredient in ingredient_list:
                count += 1
    print(count)


def part2():
    allergens = list(allergen_map.keys())
    allergens.sort()
    print('sorted allergens', allergens)
    bad_list = []
    for allergen in allergens:
        bad_list.append(allergen_map[allergen])
    print(','.join(bad_list))


part1()
part2()
