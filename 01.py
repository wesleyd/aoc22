!/usr/bin/env python3

example = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

example.split("\n\n")

def sum_group(group):
    return sum(map(int, group.strip().split("\n")))

assert sum_group("42\n43\n41") == 126

def parse(input):
    groups = input.split("\n\n")
    return list(map(sum_group, groups))

assert parse(example) == [6000, 4000, 11000, 24000, 10000]

def day01a(input):
    return max(parse(input))

assert day01a(example) == 24000

with open('day01.txt') as f:
    print("Day01a =>", day01a(f.read()))

def day01b(input):
    return sum(sorted(parse(input))[-3:])

assert day01b(example) == 45000

with open('day01.txt') as f:
    print("Day01b =>", day01b(f.read()))
