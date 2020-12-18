def fuel(mass):
    required_fuel = mass // 3 - 2
    return max(required_fuel, 0)

# part 1
with open('input.txt') as f:
    lines = f.read().splitlines()

total_fuel = 0

for line in lines:
    mass = int(line)
    total_fuel += fuel(mass)

print(f'The required fuel for part 1 is {total_fuel}')

# Part 2
total_fuel = 0

for line in lines:
    mass = int(line)
    current_fuel = fuel(mass)
    while current_fuel > 0:
        total_fuel += current_fuel
        current_fuel = fuel(current_fuel)

print(f'\nThe required fuel for part 2 is {total_fuel}')
