with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

i = 50
sol = 0

for line in puzzle_input:
    direction = line[0]
    amount = int(line[1:])

    if direction == 'L':
        i = (i - amount) % 100
    else: #direction == 'R'
        i = (i + amount) % 100

    if i == 0:
        sol += 1

    #print(i)

print(sol)