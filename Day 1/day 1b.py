with open('input.txt') as f:
    lines = f.read().splitlines()

answer = 0

for line in lines:
    line_fuel = 0
    fuel = (int(line) // 3 - 2)
    line_fuel += fuel
    while fuel > 5:  # 6 // 3 - 2 == 0
        line_fuel += fuel // 3 - 2
        fuel = fuel // 3 - 2
    answer += line_fuel

print(f'The answer = {answer}')
