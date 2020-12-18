from copy import deepcopy
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open('input.txt') as f:
    lines = f.read().splitlines()

portal_id = None
portals = {}
visited = None
maze_01 = None


def print_maze(maze):
    for line in maze:
        print('')
        for char in line:
            print(char, end='')


def rewrite_maze(maze):
    maze = deepcopy(maze)
    maze_01 = []
    for line in maze:
        maze_01.append([])
        for char in line:
            if char == '.':
                maze_01[-1].append(1)
            else:
                maze_01[-1].append(0)
    return maze_01


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


def find_goals(start_data):
    cur_goals = []
    cur_portal = start_data[0]
    index = start_data[1]
    cur_pos = portals[cur_portal][index]
    for portal in portal_id:
        if portal in visited:
            # Do not return to already visited portals
            steps = []
            val = 0
        elif portal == 'ZZ':
            steps = run_maze(maze_01, cur_pos, portals[portal][0])
            val = 0
        else:
            steps_1 = run_maze(maze_01, cur_pos, portals[portal][0])
            steps_2 = run_maze(maze_01, cur_pos, portals[portal][1])
            if len(steps_1) > len(steps_2):
                steps = steps_1
                val = 1
            else:
                steps = steps_2
                val = 0
        if len(steps) > 0:
            cur_goals.append((portal, val, len(steps) - 1))
    return cur_goals


portals = {}
string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = list(string)
maze_chars = ['.', '#']
x_max = len(lines[0])
y_max = len(lines)

maze = []
x = None

for y in range(y_max):
    maze.append([])
    for x in range(x_max):
        if lines[y][x] in letters:
            if y == 0:
                portal = lines[y][x] + lines[y + 1][x]
                if portal not in portals:
                    portals[portal] = [(x, y + 2)]
                else:
                    portals[portal].append((x, y + 2))
            elif y == y_max - 1:
                portal = lines[y - 1][x] + lines[y][x]
                if portal not in portals:
                    portals[portal] = [(x, y - 2)]
                else:
                    portals[portal].append((x, y - 2))
            elif x == 0:
                portal = lines[y][x] + lines[y][x + 1]
                if portal not in portals:
                    portals[portal] = [(x + 2, y)]
                else:
                    portals[portal].append((x + 2, y))
            elif x == x_max - 1:
                portal = lines[y][x - 1] + lines[y][x]
                if portal not in portals:
                    portals[portal] = [(x - 2, y)]
                else:
                    portals[portal].append((x - 2, y))
            elif 5 < x < x_max - 5 and 5 < y < y_max - 5:
                # Middle portal
                if lines[y][x + 1] in letters and lines[y][x - 1] in maze_chars:
                    portal = lines[y][x] + lines[y][x + 1]
                    if portal not in portals:
                        portals[portal] = [(x - 1, y)]
                    else:
                        portals[portal].append((x - 1, y))
                elif lines[y][x - 1] in letters and lines[y][x + 1] in maze_chars:
                    portal = lines[y][x - 1] + lines[y][x]
                    if portal not in portals:
                        portals[portal] = [(x + 1, y)]
                    else:
                        portals[portal].append((x + 1, y))
                elif lines[y + 1][x] in letters and lines[y - 1][x] in maze_chars:
                    portal = lines[y][x] + lines[y + 1][x]
                    if portal not in portals:
                        portals[portal] = [(x, y - 1)]
                    else:
                        portals[portal].append((x, y - 1))
                elif lines[y - 1][x] in letters and lines[y + 1][x] in maze_chars:
                    portal = lines[y - 1][x] + lines[y][x]
                    if portal not in portals:
                        portals[portal] = [(x, y + 1)]
                    else:
                        portals[portal].append((x, y + 1))
        if lines[y][x] not in maze_chars:
            maze[-1].append('#')
        else:
            maze[-1].append(lines[y][x])


# Assumption --> Portals are not short-circuited (portal end always in other area than portal start)
portal_id = sorted(list(portals.keys()))
maze_01 = rewrite_maze(maze)
visited = ['AA']
cur_pos = portals['AA'][0]
start_data = ('AA', 0, 0)
route = []
path_len = [0]

# cur_goals = [portal, exit_index, steps to get to portal]
route.append(find_goals(start_data))
shortest_path = 99999999999999999999

while True:
    # Check if anything left in route
    if len(route) == 0:
        print('All paths followed')
        break
    # Check if route available; if not go back 1 level
    if len(route[-1]) == 0:
        del route[-1]
        del visited[-1]
        del path_len[-1]
        print(f'go level up, current route = {route}')
        continue
    # choose new path, and go to next level
    go_to = route[-1][0]
    if go_to[0] == 'ZZ':
        # goal reached
        cur_path = sum(path_len) + go_to[2]
        if cur_path < shortest_path:
            shortest_path = cur_path
        # Remove 'ZZ' and continue
        route[-1].remove(go_to)
        continue
    else:
        print(f'go level down, current route = {route}')
        route[-1].remove(go_to)
        visited.append(go_to[0])
        path_len.append(go_to[2] + 1)
        route.append(find_goals(go_to))

print(f'The answer is {shortest_path}')

