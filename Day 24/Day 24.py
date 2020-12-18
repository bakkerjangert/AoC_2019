from copy import deepcopy

with open('input.txt') as f:
    lines = f.read().splitlines()

def print_grid():
    print(f'\n---Printing current grid---')
    for line in grid:
        print('')
        for char in line:
            print(char, end='')
    print('')


def bio_diversity():
    rating = 1
    total = 0
    for line in grid:
        for char in line:
            if char == '#':
                total += rating
            rating *= 2
    return total

grid = []
encoutered = set(())

cur_layout = ''
for line in lines:
    cur_layout += line
    grid.append([])
    for char in line:
        grid[-1].append(char)
encoutered.add(cur_layout)

print_grid()

while True:
    prev_grid = deepcopy(grid)
    for y in range(len(prev_grid)):
        for x in range(len(prev_grid[0])):
            count_adjacent_bugs = 0
            for delta in (-1, 1):
                if y + delta < 0 or y + delta >= len(grid):
                    pass
                elif prev_grid[y + delta][x] == '#':
                    count_adjacent_bugs += 1
                if x + delta < 0 or x + delta >= len(grid[0]):
                    pass
                elif prev_grid[y][x + delta] == '#':
                    count_adjacent_bugs += 1
            if prev_grid[y][x] == '#' and count_adjacent_bugs != 1:
                grid[y][x] = '.'
            if prev_grid[y][x] == '.' and (count_adjacent_bugs == 1 or count_adjacent_bugs == 2):
                grid[y][x] = '#'
    print_grid()
    cur_layout = ''
    for line in grid:
        cur_layout += ''.join(line)
    if cur_layout in encoutered:
        print('current layout found twice!')
        break
    else:
        encoutered.add(cur_layout)

answer = bio_diversity()

print(f'The answer is {answer}')
