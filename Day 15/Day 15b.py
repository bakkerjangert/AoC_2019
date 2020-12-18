import random
from copy import deepcopy
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from Astar import Astar

with open('input.txt') as f:
    lines = f.read().splitlines()

prog_lst = list(map(int, lines[0].split(',')))

prog = {}

for i in range(len(prog_lst)):
    prog[i] = prog_lst[i]

# Note --> In code below the <try - except> reads not yet known memory as value 0


def op_1(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        try:
            val_1 = prog[pos + 1]
        except KeyError:
            val_1 = 0
    elif code[2] == '2':
        try:
            val_1 = prog[rel_val + index_1]
        except KeyError:
            val_1 = 0
    elif code[2] == '0':
        try:
            val_1 = prog[index_1]
        except KeyError:
            val_1 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        try:
            val_2 = prog[pos + 2]
        except KeyError:
            val_2 = 0
    elif code[1] == '2':
        try:
            val_2 = prog[rel_val + index_2]
        except KeyError:
            val_2 = 0
    elif code[1] == '0':
        try:
            val_2 = prog[index_2]
        except KeyError:
            val_2 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    # write value
    if code[0] == '1':
        prog[pos + 3] = val_1 + val_2
    elif code[0] == '2':
        prog[rel_val + index_3] = val_1 + val_2
    elif code[0] == '0':
        prog[index_3] = val_1 + val_2
    else:
        print('Error! Unknown method code!')
        exit()
    pos += 4
    return pos


def op_2(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        try:
            val_1 = prog[pos + 1]
        except KeyError:
            val_1 = 0
    elif code[2] == '2':
        try:
            val_1 = prog[index_1 + rel_val]
        except KeyError:
            val_1 = 0
    elif code[2] == '0':
        try:
            val_1 = prog[index_1]
        except KeyError:
            val_1 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        try:
            val_2 = prog[pos + 2]
        except KeyError:
            val_2 = 0
    elif code[1] == '2':
        try:
            val_2 = prog[rel_val + index_2]
        except KeyError:
            val_2 = 0
    elif code[1] == '0':
        try:
            val_2 = prog[index_2]
        except KeyError:
            val_2 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    # Write value
    if code[0] == '1':
        prog[pos + 3] = val_1 * val_2
    elif code[0] == '2':
        prog[rel_val + index_3] = val_1 * val_2
    elif code[0] == '0':
        prog[index_3] = val_1 * val_2
    else:
        print('Error! Unknown method code!')
        exit()
    pos += 4
    return pos


def op_3(prog, pos, input_val, rel_val):
    index_1 = prog[pos + 1]
    code = str(prog[pos])
    while len(code) < 3:
        code = '0' + code
    if code[0] == '1':
        prog[pos + 1] = input_val
    elif code[0] == '2':
        prog[rel_val + index_1] = input_val
    elif code[0] == '0':
        prog[index_1] = input_val
    else:
        print('Error! Unknown method code!')
        exit()
    pos += 2
    return pos


def op_4(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    code = str(prog[pos])
    while len(code) < 3:
        code = '0' + code
    if code[0] == '1':
        try:
            output = prog[pos + 1]
        except KeyError:
            output = 0
    elif code[0] == '2':
        try:
            output = prog[rel_val + index_1]
        except KeyError:
            output = 0
    elif code[0] == '0':
        try:
            output = prog[index_1]
        except KeyError:
            output = 0
    else:
        print('Error! Unknown method code!')
        exit()
    pos += 2
    # print(f'Output = {output}')
    return pos, output


def op_5(prog, pos, rel_val):
    change = False
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        try:
            val_1 = prog[pos + 1]
        except KeyError:
            val_1 = 0
    elif code[2] == '2':
        try:
            val_1 = prog[rel_val + index_1]
        except KeyError:
            val_1 = 0
    elif code[2] == '0':
        try:
            val_1 = prog[index_1]
        except KeyError:
            val_1 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        try:
            val_2 = prog[pos + 2]
        except KeyError:
            val_2 = 0
    elif code[1] == '2':
        try:
            val_2 = prog[rel_val + index_2]
        except KeyError:
            val_2 = 0
    elif code[1] == '0':
        try:
            val_2 = prog[index_2]
        except KeyError:
            val_2 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    if val_1 != 0:  # Check wether this still works for Day 9
        pos = val_2
        change = True
    if not change:
        pos += 3  # Check --> This op only regards 2 values; should be +3 instead of +4?
    return pos


def op_6(prog, pos, rel_val):
    change = False
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        try:
            val_1 = prog[pos + 1]
        except KeyError:
            val_1 = 0
    elif code[2] == '2':
        try:
            val_1 = prog[rel_val + index_1]
        except KeyError:
            val_1 = 0
    elif code[2] == '0':
        try:
            val_1 = prog[index_1]
        except KeyError:
            val_1 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        try:
            val_2 = prog[pos + 2]
        except KeyError:
            val_2 = 0
    elif code[1] == '2':
        try:
            val_2 = prog[rel_val + index_2]
        except KeyError:
            val_2 = 0
    elif code[1] == '0':
        try:
            val_2 = prog[index_2]
        except KeyError:
            val_2 = 0
    else:
        print('Error! Unknown methode code!')
        exit()
    if val_1 == 0:  # Check wether this still works for Day 9
        pos = val_2
        change = True
    if not change:
        pos += 3  # Check --> This op only regards 2 values; should be +3 instead of +4?
    return pos


def op_7(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        try:
            val_1 = prog[pos + 1]
        except KeyError:
            val_1 = 0
    elif code[2] == '2':
        try:
            val_1 = prog[rel_val + index_1]
        except KeyError:
            val_1 = 0
    elif code[2] == '0':
        try:
            val_1 = prog[index_1]
        except KeyError:
            val_1 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        try:
            val_2 = prog[pos + 2]
        except KeyError:
            val_2 = 0
    elif code[1] == '2':
        try:
            val_2 = prog[rel_val + index_2]
        except KeyError:
            val_2 = 0
    elif code[1] == '0':
        try:
            val_2 = prog[index_2]
        except KeyError:
            val_2 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    if val_1 < val_2:
        if code[0] == '1':
            prog[pos + 3] = 1
        elif code[0] == '2':
            prog[rel_val + index_3] = 1
        elif code[0] == '0':
            prog[index_3] = 1
        else:
            print('Error! Unknown method code!')
            exit()
    else:
        if code[0] == '1':
            prog[pos + 3] = 0
        elif code[0] == '2':
            prog[rel_val + index_3] = 0
        elif code[0] == '0':
            prog[index_3] = 0
        else:
            print('Error! Unknown method code!')
            exit()
    pos += 4
    return pos


def op_8(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        try:
            val_1 = prog[pos + 1]
        except KeyError:
            val_1 = 0
    elif code[2] == '2':
        try:
            val_1 = prog[rel_val + index_1]
        except KeyError:
            val_1 = 0
    elif code[2] == '0':
        try:
            val_1 = prog[index_1]
        except KeyError:
            val_1 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        try:
            val_2 = prog[pos + 2]
        except KeyError:
            val_2 = 0
    elif code[1] == '2':
        try:
            val_2 = prog[rel_val + index_2]
        except KeyError:
            val_2 = 0
    elif code[1] == '0':
        try:
            val_2 = prog[index_2]
        except KeyError:
            val_2 = 0
    else:
        print('Error! Unknown method code!')
        exit()
    if val_1 == val_2:
        if code[0] == '1':
            prog[pos + 3] = 1
        elif code[0] == '2':
            prog[rel_val + index_3] = 1
        elif code[0] == '0':
            prog[index_3] = 1
        else:
            print('Error! Unknown method code!')
            exit()
    else:
        if code[0] == '1':
            prog[pos + 3] = 0
        elif code[0] == '2':
            prog[rel_val + index_3] = 0
        elif code[0] == '0':
            prog[index_3] = 0
        else:
            print('Error! Unknown method code!')
            exit()
    pos += 4
    return pos


def op_9(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    code = str(prog[pos])
    while len(code) < 3:
        code = '0' + code
    if code[0] == '1':
        try:
            rel_val += prog[pos + 1]
        except KeyError:
            pass
    elif code[0] == '2':
        try:
            rel_val += prog[rel_val + index_1]
        except KeyError:
            pass
    elif code[0] == '0':
        try:
            rel_val += prog[index_1]
        except KeyError:
            pass
    else:
        print('Error! Unknown method code!')
        exit()
    pos += 2
    return pos, rel_val

def get_target(bot_pos, input_val):
    if input_val == 1:
        return bot_pos[0], bot_pos[1] - 1
    elif input_val == 2:
        return bot_pos[0], bot_pos[1] + 1
    elif input_val == 3:
        return bot_pos[0] - 1, bot_pos[1]
    elif input_val == 4:
        return bot_pos[0] + 1, bot_pos[1]
    else:
        print(f'Error: input value not understood!')
        exit()

def update_bot_pos(bot_pos, input_val):
    if input_val == 1:
        bot_pos[1] -= 1
    elif input_val == 2:
        bot_pos[1] += 1
    elif input_val == 3:
        bot_pos[0] -= 1
    elif input_val == 4:
        bot_pos[0] += 1
    else:
        print(f'Error: input value not understood!')
        exit()

def count_adjacent(bot_pos, board_data):
    x = bot_pos[0]
    y = bot_pos[1]
    count = 0
    if tuple((x - 1, y)) in board_data:
        count += 1
    if tuple((x + 1, y)) in board_data:
        count += 1
    if tuple((x, y - 1)) in board_data:
        count += 1
    if tuple((x, y + 1)) in board_data:
        count += 1
    return count

def opposite(input_val):
    opposite_val = None
    if input_val == 1:
        opposite_val = 2
    elif input_val == 2:
        opposite_val = 1
    elif input_val == 3:
        opposite_val = 4
    elif input_val == 4:
        opposite_val = 3
    return opposite_val

def print_data(board_data, bot_pos, finish):
    grid_bot = board_data.copy()
    grid_bot[tuple(bot_pos)] = 'B'
    xy = list(grid_bot.keys())
    xy.sort()
    x_min = xy[0][0]
    x_max = xy[-1][0]
    xy.sort(key=lambda x: x[1])
    y_min = xy[0][-1]
    y_max = xy[-1][-1]
    grid = []
    for y in range(y_max - y_min + 1):
        grid.append([])
        for x in range(x_max - x_min + 1):
            grid[-1].append('*')
    for k, v in grid_bot.items():
        x = k[0] - x_min
        y = k[1] - y_min
        grid[y][x] = v
    grid[-y_min][-x_min] = 'S'
    if finish is not None:
        grid[finish[1] - y_min][finish[0] - x_min] = 'F'
    # print(f'\n----Printing Grid----')
    # for k, v in grid_bot.items():
    #     print(f'{k} --> {v}')
    for line in grid:
        print('')
        for char in line:
            print(char, end='')
    print('')
    return grid

def get_open_dir(bot_pos, board_data):
    open_dir = []
    path = []
    direction = 1
    for i in range(4):
        if get_target(bot_pos, direction) not in board_data:
            open_dir.append(direction)
        elif board_data[get_target(bot_pos, direction)] == '.':
            path.append(direction)
        direction += 1
    return open_dir, path

def check_maze(board_data):
    grid = print_data(board_data, bot_pos, finish)
    x_max = len(grid[0])
    y_max = len(grid)
    for x in range(x_max):
        for y in range(y_max):
            if grid[y][x] == '.':
                if x == 0 or y == 0 or x == x_max or y == y_max:
                    print('failed on boundary')
                    return False
                elif grid[y][x+1] == '*' or grid[y][x-1] == '*' or grid[y + 1][x] == '*' or grid[y - 1][x] == '*':
                    print('failed on * next to .')
                    return False
                else:
                    continue
    return True

def print_maze(maze):
    for line in maze:
        print('')
        for char in line:
            print(char, end='')

rel_val = 0

output = None
pos = 0

bot_pos = [0, 0]
board_data = {}
board_data[tuple(bot_pos)] = '.'
return_point = [[]]
returning = False

input_val = 1 # start north
iter = 0
finish = None
while True:
    icode = prog[pos] % 100
    if icode == 1:
        pos = op_1(prog, pos, rel_val)
    elif icode == 2:
        pos = op_2(prog, pos, rel_val)
    elif icode == 3:
        pos = op_3(prog, pos, input_val, rel_val)
    elif icode == 4:
        tup = op_4(prog, pos, rel_val)
        pos = tup[0]
        output = tup[1]
        # Day 15:
        iter += 1
        if iter % 10000 == 0:
            print_data(board_data, bot_pos, finish)
            if check_maze(board_data):
                print(f'Maze is finalized, full path found')
                grid = print_data(board_data,bot_pos, finish)
                break
        target = get_target(bot_pos, input_val)
        if output == 0:
            board_data[target] = '#'
            data = get_open_dir(bot_pos, board_data)
            if len(data[0]) != 0:
                input_val = random.choice(data[0])
            else:
                input_val = random.choice(data[1])
        elif output == 1:
            update_bot_pos(bot_pos, input_val)
            board_data[tuple(bot_pos)] = '.'
            data = get_open_dir(bot_pos, board_data)
            if len(data[0]) != 0:
                input_val = random.choice(data[0])
            else:
                if len(data[1]) > 1:
                    data[1].remove(opposite(input_val))
                input_val = random.choice(data[1])
        elif output == 2:
            update_bot_pos(bot_pos, input_val)
            board_data[tuple(bot_pos)] = 'F'
            finish = tuple(bot_pos)
            data = get_open_dir(bot_pos, board_data)
            if len(data[0]) != 0:
                input_val = random.choice(data[0])
            else:
                input_val = random.choice(data[1])
    elif icode == 5:
        pos = op_5(prog, pos, rel_val)
    elif icode == 6:
        pos = op_6(prog, pos, rel_val)
    elif icode == 7:
        pos = op_7(prog, pos, rel_val)
    elif icode == 8:
        pos = op_8(prog, pos, rel_val)
    elif icode == 9:
        tup = op_9(prog, pos, rel_val)
        pos = tup[0]
        rel_val = tup[1]
    elif icode == 99:
        print(f'End of Int Machine')
        break
    else:
        print('Danger! Danger! Unknown input command!!!')
        break

org_grid = deepcopy(grid)

start = None
end = None
x_max = len(grid[0])
y_max = len(grid)


for x in range(x_max):
    for y in range(y_max):
        if grid[y][x] == 'B':
            grid[y][x] = 1
            org_grid[y][x] = '.'
        elif grid[y][x] == 'S':
            start = (x, y)
            grid[y][x] = 1
        elif grid[y][x] == 'F':
            end = (x, y)
            grid[y][x] = 1
        elif grid[y][x] == '.':
            grid[y][x] = 1
        else:
            grid[y][x] = 0

solve_grid = Grid(matrix=grid)
start_point = solve_grid.node(start[0], start[1])
end_point = solve_grid.node(end[0], end[1])

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start_point, end_point, solve_grid)

print('operations:', runs, 'path length:', len(path))
print(solve_grid.grid_str(path=path, start=start_point, end=end_point))

# Note the the Astar finder returns whole length, including start_point

print(f'The answer to part 1 is {len(path) - 1}')

maze = deepcopy(org_grid)
maze[start[1]][start[0]] = '.'
maze[end[1]][end[0]] = 'O'

dot_count = 0
for line in maze:
    for char in line:
        if char == '.':
            dot_count += 1
total_dot = dot_count



step = 0
while dot_count != 0:
    step += 1
    # if step % 10 == 0:
    #     print_maze(maze)
    #     breakpoint()
    print(f'Currently {round(((total_dot - dot_count) / total_dot),3) * 100}% is filled')
    for y in range(y_max):
        for x in range(x_max):
            if maze[y][x] == 'O':
                # Temporry set on P value to prevent multiple steps per iteration
                if maze[y - 1][x] == '.':
                    maze[y - 1][x] = 'P'
                    dot_count -= 1
                if maze[y + 1][x] == '.':
                    maze[y + 1][x] = 'P'
                    dot_count -= 1
                if maze[y][x - 1] == '.':
                    maze[y][x - 1] = 'P'
                    dot_count -= 1
                if maze[y][x + 1] == '.':
                    maze[y][x + 1] = 'P'
                    dot_count -= 1
    for y in range(y_max):
        for x in range(x_max):
            # At end replace all temporary P values to O values
            if maze[y][x] == 'P':
                maze[y][x] = 'O'

for line in maze:
    print('')
    for char in line:
        print(char, end='')

print(f'\nThe answer to part 2 = {step}')
