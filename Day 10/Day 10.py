from fractions import Fraction
from copy import deepcopy

with open('input.txt') as f:
    lines = f.read().splitlines()

def print_grid(grid):
    print(f'\n------')
    for line in grid:
        for char in line:
            print(char, end='')
        print('')


def get_angles(grid, x, y):
    x_min = -x
    y_min = -y
    x_max = len(grid[0]) - x
    y_max = len(grid) - y
    angles = []
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if y == 0:
                pass
            else:
                denom = Fraction(x, y).denominator
                num = Fraction(x, y).numerator
                angle = (num, denom)
                if angle not in angles:
                    angles.append(angle)
        angles.append((1, 0))
        angles = sorted(set(angles))
    return angles


def sub_count(grid, x, y):
    angles = get_angles(grid, x, y)
    # Positive angles
    for angle in angles:
        cur_x = x
        cur_y = y
        while True:
            cur_x += angle[0]
            cur_y += angle[1]
            if cur_x < 0 or cur_y < 0:
                break
            try:
                if grid[cur_y][cur_x] != '.':
                    grid[cur_y][cur_x] = '1'
                    break
            except IndexError:
                break
    # Negative angles
    for angle in angles:
        cur_x = x
        cur_y = y
        while True:
            cur_x -= angle[0]
            cur_y -= angle[1]
            if cur_x < 0 or cur_y < 0:
                break
            try:
                if grid[cur_y][cur_x] != '.':
                    grid[cur_y][cur_x] = '1'
                    break
            except IndexError:
                break
    grid[y][x] = 'W'
    count = 0
    print('\n----')
    for line in grid:
        for char in line:
            if char.isdigit():
                count += 1
            print(char, end='')
        print('')
    print(count)
    return count

grid = []

for line in lines:
    grid.append([])
    for char in line:
        grid[-1].append(char)



# cur_count = sub_count(deepcopy(grid), 5, 8)
# exit()

count = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '#':
            cur_count = sub_count(deepcopy(grid), x, y)
            if cur_count > count:
                count = cur_count

print(f'The answer is {count}')






