from fractions import Fraction
from copy import deepcopy
import math

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
                if x != 0:
                    angle = (num, denom, y / x)
                else:
                    angle = (num, denom, 99999)
                if angle not in angles:
                    angles.append(angle)
        angles.append((1, 0, 0))
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
    # print('\n----')
    for line in grid:
        for char in line:
            if char.isdigit():
                count += 1
            # print(char, end='')
        # print('')
    # print(count)
    return count

def shoot(grid, x, y, angles):
    limit = 200
    count = 0
    while True:
        for angle in angles:
            cur_x = x
            cur_y = y
            while True:
                cur_x += angle[0]
                cur_y += angle[1]
                if cur_x < 0 or cur_y < 0:
                    break
                try:
                    if grid[cur_y][cur_x] == '#':
                        count += 1
                        grid[cur_y][cur_x] = 'X'
                        # print_grid(grid)
                        print(f'shot {count} destroys {cur_x,cur_y}')
                        if count == limit:
                            return cur_x, cur_y
                        grid[cur_y][cur_x] = '.'
                        break
                except IndexError:
                    break
        # Continue to next cycle of laser

grid = []

for line in lines:
    grid.append([])
    for char in line:
        grid[-1].append(char)

# cur_count = sub_count(deepcopy(grid), 5, 8)
# exit()

# count = 0
# pos = (0, 0)
# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == '#':
#             cur_count = sub_count(deepcopy(grid), x, y)
#             if cur_count > count:
#                 count = cur_count
#                 pos = (x, y)

# print(f'The answer is {count} at pos {pos}')

pos = (27, 19)

# TEST
# pos = (11, 13)

shoot_angle = get_angles(grid, pos[0], pos[1])
angle_pos = []
angle_neg = []

for angle in shoot_angle:
    if angle[2] < 0:
        angle_neg.append(angle)
    else:
        angle_pos.append(angle)

angle_pos = sorted(angle_pos, key=lambda x: x[2])
angle_neg = sorted(angle_neg, key=lambda x: x[2])

angle_sorted = []

angle_sorted.append((angle_pos[-1][0] * -1, angle_pos[-1][1] * -1))
for angle in angle_neg:
    angle_sorted.append((angle[0] * -1, angle[1] * -1))
for angle in angle_pos:
    angle_sorted.append((angle[0], angle[1]))
for angle in angle_neg:
    angle_sorted.append((angle[0], angle[1]))
for angle in angle_pos:
    angle_sorted.append((angle[0] * -1, angle[1] * -1))
del angle_sorted[-1]

# print(angle_sorted)

target = shoot(grid, pos[0], pos[1], angle_sorted)

print(f'the answer = {100 * target[0] + target[1]}')
