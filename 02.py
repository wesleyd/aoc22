#!/usr/bin/env python3

example = """\
A Y
B X
C Z\
"""

def parse(input):
    return [line.split() for line in input.splitlines()]

assert parse(example) == [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

# chr(ord('X') - ord('X') + ord('A'))

def score(pair):
    them, me = pair
    # Rock (A) is 1, Paper (B) is 2, Scissors (C) is 3.
    p = ord(me) - ord('X') + 1
    # 0 for a loss, 3 for a draw, 6 for a win
    delta = (ord(me) - ord('X')) - (ord(them) - ord('A'))
    if delta == 0:  # A draw
        q = 3
    elif delta == 1 or delta == -2:
        q = 6
    elif delta == 2 or delta == -1:
        q = 0
    else:
        raise Exception(f"Bad score ({a}, {b}) => delta={delta}")
    return p+q

assert score(['A', 'Y']) == 8
assert score(['B', 'X']) == 1
assert score(['C', 'Z']) == 6

def part1(input):
    return sum(map(score, parse(input)))

assert part1(example) == 15

with open('day02.txt') as f:
    print("Day02 part 1 => ", part1(f.read()))  # => 15632

guide = {
    ('A', 'X'): 'C',
    ('B', 'X'): 'A',
    ('C', 'X'): 'B',
    ('A', 'Y'): 'A',
    ('B', 'Y'): 'B',
    ('C', 'Y'): 'C',
    ('A', 'Z'): 'B',
    ('B', 'Z'): 'C',
    ('C', 'Z'): 'A',
}

def score2(pair):
    them, goal = pair
    me = guide[(them, goal)]
    # Rock (A) is 1, Paper (B) is 2, Scissors (C) is 3.
    p = ord(me) - ord('A') + 1
    q = (ord(goal) - ord('X')) * 3
    return p+q

assert score2(['A', 'Y']) == 4
assert score2(['B', 'X']) == 1
assert score2(['C', 'Z']) == 7

def part2(input):
    return sum(map(score2, parse(input)))

assert part2(example) == 12

with open('day02.txt') as f:
    print("Day02 part 2 => ", part2(f.read()))  # => 14416
