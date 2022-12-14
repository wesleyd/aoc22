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

def score(moves):
    them, me = moves
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
    print("Day02 part 1 => ", part1(f.read()))

