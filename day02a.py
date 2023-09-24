#!/usr/bin/env python3

import itertools

from unittest import TestCase as tc

example_input = """
A Y
B X
C Z
"""

def parse(inp):
    moves = inp.split()
    for i in range(0, len(moves), 2):
        yield (moves[i], moves[i+1])

LOOKUP = [3, 0, 6]

def score(move):
    a = ord(move[0]) - ord('A') + 1
    x = ord(move[1]) - ord('X') + 1
    d = (a-x)%3
    return x + LOOKUP[d]
tc().assertEqual(score(['A', 'Y']), 8)
tc().assertEqual(score(['B', 'X']), 1)
tc().assertEqual(score(['C', 'Z']), 6)

def play(inp):
    for move in parse(inp):
        yield score(move)

def run(inp):
    return sum(play(inp))

with open("day02.txt", "r") as f:
    real_input = f.read()

print(run(real_input))  # 15632
