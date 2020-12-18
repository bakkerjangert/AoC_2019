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
        # For part 2 Portals can be visited multiple times
        # print(f'Check in visited --> { tuple((portal, cur_level))}')
        next_level = depth_level[-1] + portals[portal]
        if tuple((portal, depth_level[-1])) in visited:
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
    sorted_goals = []
    # Goals to be sorted so level decreasing portals analysed first
    for item in cur_goals:
        portal = item[0]
        index = item[1]
        if portals[portal][index][2] == -1:
            sorted_goals.insert(-1, item)
        else:
            sorted_goals.insert(0, item)
    return sorted_goals


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
                portal = lines[y][x] + lines[y + 1][x] + '-'
                portals[portal] = (x, y + 2)
            elif y == y_max - 1:
                portal = lines[y - 1][x] + lines[y][x] + '-'
                portals[portal] = (x, y - 2)
            elif x == 0:
                portal = lines[y][x] + lines[y][x + 1] + '-'
                portals[portal] = (x + 2, y)
            elif x == x_max - 1:
                portal = lines[y][x - 1] + lines[y][x] + '-'
                portals[portal] = (x - 2, y)
            elif 5 < x < x_max - 5 and 5 < y < y_max - 5:
                if lines[y][x + 1] in letters and lines[y][x - 1] in maze_chars:
                    portal = lines[y][x] + lines[y][x + 1] + '+'
                    portals[portal] = (x - 1, y)
                elif lines[y][x - 1] in letters and lines[y][x + 1] in maze_chars:
                    portal = lines[y][x - 1] + lines[y][x] + '+'
                    portals[portal] = (x + 1, y)
                elif lines[y + 1][x] in letters and lines[y - 1][x] in maze_chars:
                    portal = lines[y][x] + lines[y + 1][x] + '+'
                    portals[portal] = (x, y - 1)
                elif lines[y - 1][x] in letters and lines[y + 1][x] in maze_chars:
                    portal = lines[y - 1][x] + lines[y][x] + '+'
                    portals[portal] = (x, y + 1)
        if lines[y][x] not in maze_chars:
            maze[-1].append('#')
        else:
            maze[-1].append(lines[y][x])


# Assumption --> Portals are not short-circuited (portal end always in other area than portal start)
portal_id = sorted(list(portals.keys()))

for portal in portal_id:
    print(f'{portal} --> {portals[portal]}')

# Run once to create underlying dict
# maze_01 = rewrite_maze(maze)
# portal_paths = {}
# for portal_1 in portal_id:
#     start_point = portals[portal_1]
#     for portal_2 in portal_id:
#         if portal_1 == portal_2:
#             continue
#         end_point = portals[portal_2]
#         cur_path = run_maze(maze_01, start_point, end_point)
#         if len(cur_path) > 0:
#             if portal_1 not in portal_paths:
#                 portal_paths[portal_1] = [(portal_2, len(cur_path))]
#             else:
#                 portal_paths[portal_1].append((portal_2, len(cur_path)))


portal_paths = {'AA-': [('YL+', 53)],
                'AC+': [('MV-', 45), ('ZZ-', 47)],
                'AC-': [('YJ+', 55)],
                'FW+': [('JL+', 5), ('UJ-', 55), ('YM-', 51), ('FW+', 1)],
                'FW-': [('MF+', 61)],
                'IJ+': [('SC-', 61)],
                'IJ-': [('PS+', 45)],
                'JA+': [('OY-', 37)],
                'JA-': [('SD+', 53)],
                'JL+': [('FW+', 5), ('UJ-', 53), ('YM-', 49), ('JL+', 1)],
                'JL-': [('JQ+', 51)],
                'JQ+': [('JL-', 51)],
                'JQ-': [('KQ+', 49)],
                'KQ+': [('JQ-', 49)],
                'KQ-': [('SC+', 53)],
                'LE+': [('YL-', 81)],
                'LE-': [('YM+', 43)],
                'MF+': [('FW-', 61)],
                'MF-': [('XQ+', 65)],
                'MV+': [('PS-', 37)],
                'MV-': [('AC+', 45), ('ZZ-', 5)],
                'NC+': [('RA-', 55)],
                'NC-': [('ND+', 59)],
                'ND+': [('NC-', 59)],
                'ND-': [('YT+', 61)],
                'OY+': [('YT-', 47)],
                'OY-': [('JA+', 37)],
                'PS+': [('IJ-', 45)],
                'PS-': [('MV+', 37)],
                'RA+': [('YJ-', 39)],
                'RA-': [('NC+', 55)],
                'SC+': [('KQ-', 53)],
                'SC-': [('IJ+', 61)],
                'SD+': [('JA-', 53)],
                'SD-': [('SJ+', 73)],
                'SJ+': [('SD-', 73)],
                'SJ-': [('UI+', 51)],
                'UI+': [('SJ-', 51)],
                'UI-': [('UJ+', 49)],
                'UJ+': [('UI-', 49)],
                'UJ-': [('FW+', 55), ('JL+', 53), ('YM-', 7), ('UJ-', 1)],
                'UX+': [('ZB-', 49)],
                'UX-': [('YL+', 57)],
                'XQ+': [('MF-', 65)],
                'XQ-': [('ZB+', 51)],
                'YJ+': [('AC-', 55)],
                'YJ-': [('RA+', 39)],
                'YL+': [('UX-', 57)],
                'YL-': [('LE+', 81)],
                'YM+': [('LE-', 43)],
                'YM-': [('FW+', 51), ('JL+', 49), ('UJ-', 7), ('YM-', 1)],
                'YT+': [('ND-', 61)],
                'YT-': [('OY+', 47)],
                'ZB+': [('XQ-', 51)],
                'ZB-': [('UX+', 49)],
                'ZZ-': [('Exit')]}

for portal in portal_id:
    print(f'{portal} --> {portal_paths[portal]}')

depth_level = 0
start_point = 'AA-'
walked = 0

plus = 13


while True:
    print(f'\n-- printing data --')
    print(f'At postition {start_point} at level {depth_level} and already taken {walked} steps')
    end_points = portal_paths[start_point]
    if len(end_points) == 1:
        end_data = end_points[0]
        walked += end_data[1]
        end_point = end_data[0]
        if end_point[2] == '+':
            depth_level += 1
            start_point = end_point[0:2] + '-'
        else:
            depth_level -= 1
            start_point = end_point[0:2] + '+'
    elif len(end_points) == 2 and depth_level != 0:
        print(f'Skipped exit at level {depth_level}!')
        end_data = end_points[0]
        walked += end_data[1]
        end_point = end_data[0]
        if end_point[2] == '+':
            depth_level += 1
            start_point = end_point[0:2] + '-'
        else:
            depth_level -= 1
            start_point = end_point[0:2] + '+'
    elif len(end_points) == 2 and depth_level == 0:
        end_data = end_points[1]
        walked += end_data[1] - 1  #Last step not required to enter portal
        print(f'Reached exit at {walked} steps!')
        break
    elif len(end_points) == 4:
        print(f'Reached fork at level {depth_level}. Choices are {end_points}')
        index = int(input('Which index do you chose?'))
        end_data = end_points[index]
        walked += end_data[1]
        end_point = end_data[0]
        if end_point[2] == '+':
            depth_level += 1
            start_point = end_point[0:2] + '-'
        else:
            depth_level -= 1
            start_point = end_point[0:2] + '+'

exit()