from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open('input.txt') as f:
    lines = f.read().splitlines()

# # Test to excel
# for line in lines:
#     print('')
#     for char in line:
#         print(char, end=', ')

def run_maze(maze, start_point, end_point):
    grid = Grid(matrix=maze)
    start = grid.node(start_point[0], start_point[1])
    end = grid.node(end_point[0], end_point[1])
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    # if len(path) > 0:
    #     print(grid.grid_str(path=path, start=start, end=end))
    #     breakpoint()
    return path


lower_key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_key = []
for char in lower_key:
    upper_key.append(char.upper())

keys_data = {}
doors_data = {}
maze = []

for y in range(len(lines)):
    maze.append([])
    for x in range(len(lines[0])):
        char = lines[y][x]
        if char in lower_key:
            keys_data[char] = tuple((x, y))
            maze[-1].append(1)
        elif char in upper_key:
            doors_data[char] = tuple((x, y))
            maze[-1].append(1)
        elif char == '@':
            start_point = tuple((x, y))
            maze[-1].append(1)
        elif char == '.':
            maze[-1].append(1)
        elif char == '#':
            maze[-1].append(0)
        else:
            print(char)
            print(f'unknown char found!')
            exit()

# order = ['u', 'o', 'x', 'e', 'n', 'q', 'b', 'f', 'm', 'i', 'w', 'c', 'k', 's', 'd', 't', 'y', 'z', 'r', 'g', 'a', 'j', 'h', 'p', 'v']
start_point_1 = (start_point[0] + 1, start_point[1] - 1)
start_point_2 = (start_point[0] + 1, start_point[1] + 1)
start_point_3 = (start_point[0] - 1, start_point[1] + 1)
start_point_4 = (start_point[0] - 1, start_point[1] - 1)

order_1 = [start_point_1, 'e', 'n', 'z', 'r', 'g', 'a', 'j', 'h', 'p', 'v']
order_2 = [start_point_2, 'u', 'o', 'x', 'm', 'i', 'w', 'c', 'k']
order_3 = [start_point_3, 's', 'd', 't', 'y']
order_4 = [start_point_4, 'q', 'b', 'f']

path_len = 0
for order in (order_1, order_2, order_3, order_4):
    start_point = order[0]
    del order[0]
    for item in order:
        print(f'\n---Going to {item} ---\n')
        end_point = keys_data[item]
        found_path = run_maze(maze, start_point, end_point)
        path_len += len(found_path) - 1  # Algorithm returns whole length including start tile
        start_point = end_point

print(f'The answer = {path_len}')




