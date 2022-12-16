#!/usr/bin/env python3

example = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

def priority(x):
    if x.islower():
        return ord(x) - ord('a') + 1
    if x.isupper():
        return ord(x) - ord('A') + 27
    raise Exception(f'Not a letter {x}.')

def rucksack(input):
    res = 0
    lines = input.splitlines()
    for line in lines:
        half = int(len(line)/2)
        a, b = set(line[:half]), set(line[half:])
        res += priority(min(a.intersection(b)))
    return res

assert rucksack(example) == 157

with open('day03.txt') as f:
    print('Day 03 part 1 => ', rucksack(f.read()))
