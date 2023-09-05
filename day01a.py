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

def parse_elves(calorie_list):
    per_elf_strings = calorie_list.split("\n\n")
    per_elf = []
    for per_elf_str in per_elf_strings:
        ss = per_elf_str.split()
        per_elf.append(sum([int(s) for s in ss]))
    return per_elf

got = parse_elves(example_calorie_list) 
want = [6000, 4000, 11000, 24000, 10000]
assert got == want, (got, want)

with open("day01.txt") as f:
    print(max(parse_elves(f.read())))
