from copy import deepcopy

with open('input.txt') as f:
    lines = f.read().splitlines()

def print_grid(grid, level):
    mid = False
    print(f'\n---Printing level {level} grid---')
    for line in grid:
        print('')
        for char in line:
            if isinstance(char, list):
                print('?', end='')
                mid = True
            else:
                print(char, end='')
    print('')
    if mid:
        print('--- ? ---')
        print(f'      [{grid[3][3][0]}]')
        print(f'[{grid[3][3][1]}]         [{grid[3][3][2]}]')
        print(f'      [{grid[3][3][3]}]')


def helping_grid(cur_level, level_plus, level_min):
    # Grid of 7 x 7 with bug counts including upper and lower levels --> Middle point = a list of 4 numbers [N, W, E, S]
    hulp_grid = []
    for y in range(7):
        hulp_grid.append([])
        for x in range(7):
            hulp_grid[-1].append(0)
            if (x == 0 and y == 0) or (x == 0 and y == 6) or (x == 6 and y == 0) or (x == 6 and y == 6):
                # edge points are always zero
                continue
            if x == 0:
                if level_min[2][1] == '#':
                    hulp_grid[y][x] += 1
            if y == 0:
                if level_min[1][2] == '#':
                    hulp_grid[y][x] += 1
            if x == 6:
                if level_min[2][3] == '#':
                    hulp_grid[y][x] += 1
            if y == 6:
                if level_min[3][2] == '#':
                    hulp_grid[y][x] += 1
            if 0 < x < 6 and 0 < y < 6:
                if cur_level[y-1][x-1] == '#':  # Note that hulp(x,y) has shifted
                    hulp_grid[y][x] += 1
    mid_point = []
    mid_point.append(0)
    for i in range(5):
        if level_plus[0][i] == '#':
            mid_point[-1] += 1
    mid_point.append(0)
    for i in range(5):
        if level_plus[i][0] == '#':
            mid_point[-1] += 1
    mid_point.append(0)
    for i in range(5):
        if level_plus[i][4] == '#':
            mid_point[-1] += 1
    mid_point.append(0)
    for i in range(5):
        if level_plus[4][i] == '#':
            mid_point[-1] += 1
    hulp_grid[3][3] = mid_point.copy()
    mid_point.clear()
    return hulp_grid

grid = []
empty_grid = []

for line in lines:
    grid.append([])
    empty_grid.append([])
    for char in line:
        grid[-1].append(char)
        empty_grid[-1].append('.')
grid[2][2] = '?'
empty_grid[2][2] = '?'

level_index = [0]
levels = {0: deepcopy(grid)}

print(f'\n--Inital state')
print_grid(levels[0], 'inital')

steps = 200
temp_grid = []

for step in range(steps):
    # First expand inward if min level has bugs
    max_level = max(level_index)
    cur_grid = deepcopy(levels[max_level])
    if cur_grid[2][1] == '#' or cur_grid[1][2] == '#' or cur_grid[3][2] == '#' or cur_grid[2][3] == '#':
        # Bug adjacent --> add level
        level_index.append(max_level + 1)
        levels[max_level + 1] = deepcopy(empty_grid)

    # Then expand outward if max level has bugs
    min_level = min(level_index)
    cur_grid = deepcopy(levels[min_level])
    bug_found = False
    for y in range(5):
        for x in range(5):
            if x == 0 or y == 0 or x == 4 or y == 4:
                if cur_grid[y][x] == '#':
                    bug_found = True
    if bug_found:
        level_index.insert(0, min_level - 1)
        levels[min_level - 1] = deepcopy(empty_grid)

    # Set initial state
    init_levels = {}
    for level in level_index:
        init_levels[level] = deepcopy(levels[level])

    # for level in level_index:
    #     print_grid(levels[level], level)

    # update per level
    for level in level_index:
        level_min = []
        level_plus = []
        cur_level = []
        if level == min(level_index):
            level_min = deepcopy(empty_grid)
        else:
            level_min = deepcopy(init_levels[level - 1])
        if level == max(level_index):
            level_plus = deepcopy(empty_grid)
        else:
            level_plus = deepcopy(init_levels[level + 1])
        cur_level = deepcopy(init_levels[level])

        # Set helping grid
        # print_grid(cur_level, level)
        # print_grid(temp_grid, 'temp')
        # breakpoint()
        count_grid = deepcopy(empty_grid)
        for y in range(5):
            for x in range(5):
                if x == 2 and y == 2:
                    # middle point
                    continue
                count_adjacent_bugs = 0
                for delta in (-1, 1):
                    # First corners level 1 --> Mind that only 0,0 and 4, 4 needed; 0,4 and 4,0 in edges
                    if x == 0 and y == 0 and delta == -1:
                        if level_min[2][1] == '#':
                            count_adjacent_bugs += 1
                        if level_min[1][2] == '#':
                            count_adjacent_bugs += 1
                    elif x == 4 and y == 4 and delta == 1:
                        if level_min[3][2] == '#':
                            count_adjacent_bugs += 1
                        if level_min[2][3] == '#':
                            count_adjacent_bugs += 1
                    # then edges to level 1
                    elif x == 0 and delta == -1:
                        if level_min[2][1] == '#':
                            count_adjacent_bugs += 1
                        if cur_level[y + delta][x] == '#':
                            count_adjacent_bugs += 1
                    elif x == 4 and delta == 1:
                        if level_min[2][3] == '#':
                            count_adjacent_bugs += 1
                        if cur_level[y + delta][x] == '#':
                            count_adjacent_bugs += 1
                    elif y == 0 and delta == -1:
                        if level_min[1][2] == '#':
                            count_adjacent_bugs += 1
                        if cur_level[y][x + delta] == '#':
                            count_adjacent_bugs += 1
                    elif y == 4 and delta == 1:
                        if level_min[3][2] == '#':
                            count_adjacent_bugs += 1
                        if cur_level[y][x + delta] == '#':
                            count_adjacent_bugs += 1
                    # Then inner parts to ?
                    elif x == 1 and y == 2 and delta == 1:
                        if cur_level[y + delta][x] == '#':
                            count_adjacent_bugs += 1
                        for y_2 in range(5):
                            if level_plus[y_2][0] == '#':
                                count_adjacent_bugs += 1
                    elif x == 3 and y == 2 and delta == -1:
                        if cur_level[y + delta][x] == '#':
                            count_adjacent_bugs += 1
                        for y_2 in range(5):
                            if level_plus[y_2][4] == '#':
                                count_adjacent_bugs += 1
                    elif x == 2 and y == 1 and delta == 1:
                        if cur_level[y][x + delta] == '#':
                            count_adjacent_bugs += 1
                        for x_2 in range(5):
                            if level_plus[0][x_2] == '#':
                                count_adjacent_bugs += 1
                    elif x == 2 and y == 3 and delta == -1:
                        if cur_level[y][x + delta] == '#':
                            count_adjacent_bugs += 1
                        for x_2 in range(5):
                            if level_plus[4][x_2] == '#':
                                count_adjacent_bugs += 1
                    # If none of above just check as if part 1
                    else:
                        if cur_level[y][x + delta] == '#':
                            count_adjacent_bugs += 1
                        if cur_level[y + delta][x] == '#':
                            count_adjacent_bugs += 1
                    count_grid[y][x] = count_adjacent_bugs
        print_grid(count_grid, level)
        for y in range(5):
            for x in range(5):
                if cur_level[y][x] == '#' and count_grid[y][x] != 1:
                    levels[level][y][x] = '.'
                if cur_level[y][x] == '.' and (count_grid[y][x] == 1 or count_grid[y][x] == 2):
                    levels[level][y][x] = '#'
        # Update level
    print(f'\n---Current levels after step {step}---')
    for level in level_index:
        print_grid(levels[level], level)
    cur_grid.clear()
    init_levels.clear()
    # breakpoint()

answer = 0
for level in level_index:
    for line in levels[level]:
        answer += line.count('#')
print(f'The answer is {answer}')

exit()