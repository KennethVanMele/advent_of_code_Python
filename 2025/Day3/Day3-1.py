with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

total_jolts = 0

for bank in puzzle_input:
    first = 0
    second = 0
    max_val = max(bank)
    imax = bank.index(max_val)
    if imax == len(bank) - 1:
        second = max_val
        first = max(bank.removesuffix(max_val))
    else:
        first = max_val
        second = max(bank[imax+1:])
    total_jolts = total_jolts + int(str(first)+str(second))

print(total_jolts)