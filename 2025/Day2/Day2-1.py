with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]
    indexes = puzzle_input[0].split(",")

invalid = []

for index in indexes:
    start  = index.split("-")[0]
    end = index.split("-")[1]
    for i in range(int(start), int(end)+1):
        half = len(str(i))//2
        p1 = str(i)[0:half]
        p2 = str(i)[half:]
        if p1 == p2:
            invalid.append(i)

print(sum(invalid))