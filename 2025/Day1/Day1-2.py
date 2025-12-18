with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

i = 50
sol = 0

for line in puzzle_input:
    direction = line[0]
    amount = int(line[1:])
    old_i = i

    #count multiple passes passed 0
    full_pass = amount //100
    sol += full_pass

    amount = amount % 100

    if direction == 'L':
        i = (i - amount) % 100
        #if old_i was zero don't count a pass
        if old_i != 0 and amount > old_i or i == 0:
            sol += 1
    else: #direction == 'R'
        i = (i + amount) % 100
        if old_i != 0 and amount + old_i >= 100 or i == 0:
            sol += 1

    #print("i:{0}".format(i))
    #print("sol:{0}".format(sol))

print(sol)