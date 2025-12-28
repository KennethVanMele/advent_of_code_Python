with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

total_jolts = 0
sol_len = 12
for bank in puzzle_input:
    stack = []
    to_remove = len(bank) - sol_len

    for battery in bank:
        while to_remove > 0 and stack and stack[-1] < battery:
            stack.pop()
            to_remove -= 1
        stack.append(battery)

    if to_remove > 0:
        stack = stack[:sol_len]

    jolt = int(''.join(stack))
    total_jolts += jolt

print(total_jolts)