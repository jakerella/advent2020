import sys
import re
from helpers import read_data_file


def get_bag_rules():
    lines = read_data_file(sys.argv[1])
    graph = {}
    for line in lines:
        bags = line.split(' bags contain ')
        if not bags[0] in graph:
            graph[bags[0]] = {}
        
        for bag in bags[1].split(', '):
            contents = re.match(r'^(\d+) (\w+ \w+) bags?\.?$', bag)
            if contents is None:
                continue
            if contents.group(2) in graph:
                if bags[0] in graph[contents.group(2)]:
                    graph[contents.group(2)][bags[0]] += int(contents.group(1))
                else:
                    graph[contents.group(2)][bags[0]] = int(contents.group(1))
            else:
                graph[contents.group(2)] = { bags[0]: int(contents.group(1)) }
    return graph

def get_bag_children():
    lines = read_data_file(sys.argv[1])
    graph = {}
    for line in lines:
        bags = line.split(' bags contain ')
        graph[bags[0]] = {}
        
        for bag in bags[1].split(', '):
            contents = re.match(r'^(\d+) (\w+ \w+) bags?\.?$', bag)
            if contents is None:
                continue
            graph[bags[0]][contents.group(2)] = int(contents.group(1))
            # if contents.group(2) in graph:
            #     if bags[0] in graph[contents.group(2)]:
            #         graph[contents.group(2)][bags[0]] += int(contents.group(1))
            #     else:
            #         graph[contents.group(2)][bags[0]] = int(contents.group(1))
            # else:
            #     graph[contents.group(2)] = { bags[0]: int(contents.group(1)) }
    return graph

def get_containers(bag, graph):
    containers = set()
    parents = list(graph[bag].keys())
    for parent in parents:
        containers.add(parent)
        for ancestor in get_containers(parent, graph):
            containers.add(ancestor)
    return containers

def count_containers(bag, graph):
    count = 0
    for child in list(graph[bag].keys()):
        count += graph[bag][child]
        count += graph[bag][child] * count_containers(child, graph)
    return count

def part1():
    rules = get_bag_rules()
    # print(rules)

    containers = get_containers('shiny gold', rules)

    # print(containers)
    print(len(containers))


def part2():
    rules = get_bag_children()
    # print(rules)

    count = count_containers('shiny gold', rules)

    print(count)


part1()
part2()
