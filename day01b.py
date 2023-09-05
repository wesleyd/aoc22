#!/usr/bin/env python3

example_calorie_list = """
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

def top_three_elves_calories(calorie_list):
    """Returns total calorie count of all elves."""
    per_elf_strings = calorie_list.split("\n\n")
    per_elf = []
    for per_elf_str in per_elf_strings:
        ss = per_elf_str.split()
        per_elf.append(sum([int(s) for s in ss]))
    return sum(sorted(per_elf, reverse=True)[:3])

got = top_three_elves_calories(example_calorie_list)
want = 45000
assert got == want, (got, want)

puzzle_input = open("day01.txt").read()

print(top_three_elves_calories(puzzle_input))
