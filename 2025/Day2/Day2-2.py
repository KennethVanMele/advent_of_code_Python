import re

def is_repeating_regex(n):
    return bool(re.match(r'^(.+)\1+$', str(n)))

with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]
    indexes = puzzle_input[0].split(",")

invalid = []

for index in indexes:
    start  = index.split("-")[0]
    end = index.split("-")[1]
    for i in range(int(start), int(end)+1):
        if is_repeating_regex(i):
            invalid.append(i)

print(sum(invalid))