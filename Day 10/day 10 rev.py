import math
with open('input.txt') as f:
    lines = f.read().splitlines()


def get_angles(dx, dy):
    angles = {0.0: (1, 0),
              90.0: (0, 1),
              180.0: (-1, 0),
              270.0: (0, -1)}
    for x in range(1, dx):
        for y in range(1, dy):
            angle = math.degrees(math.atan(y/x))
            if angle not in angles.keys() or angles[angle][0] > x:
                # First quadrant
                angles[angle] = (x, y)
                # Second quadrant
                angles[angle + 90] = (-y, x)
                # third quadrant
                angles[angle + 180] = (-x, -y)
                # fourth quadrant
                angles[angle + 270] = (y, -x)
    return angles


board = []
total_asteroids = 0
for line in lines:
    board.append([])
    for char in line:
        board[-1].append(char)
        if char == '#':
            total_asteroids += 1

height = len(board)
width = len(board[0])

total_angles = get_angles(max(height, width), max(height, width))
best_location = None
total_count = 0

for y in range(height):
    for x in range(width):
        if board[y][x] == '#':
            cur_count = 0
            for angle in sorted(total_angles.keys()):
                x_goal = x
                y_goal = y
                x_y = total_angles[angle]
                while True:
                    x_goal += x_y[0]
                    y_goal += x_y[1]
                    # First check goal is in board
                    if not (0 <= x_goal < len(board) and 0 <= y_goal < len(board)):
                        break
                    # Then check if goal is #
                    if board[y_goal][x_goal] == '#':
                        cur_count += 1
                        break
            if cur_count > total_count:
                best_location = (x, y)
                total_count = cur_count

print(f'At position {best_location} there can be seen {total_count} asteroids')

angle_list = sorted(total_angles.keys())
index = angle_list.index(270.0)
shot = 0
total_asteroids -= 1  # The one with the Laser
board[best_location[1]][best_location[0]] = 'X'

while total_asteroids > 0:
    x_goal = best_location[0]
    y_goal = best_location[1]
    x_y = total_angles[angle_list[index]]
    while True:
        x_goal += x_y[0]
        y_goal += x_y[1]
        # First check goal is in board
        if not (0 <= x_goal < len(board) and 0 <= y_goal < len(board)):
            break
        # Then check if goal is #
        if board[y_goal][x_goal] == '#':
            board[y_goal][x_goal] = '@'
            shot += 1
            total_asteroids -= 1
            if shot == 200:
                answer = x_goal * 100 + y_goal
            board[y_goal][x_goal] = '.'
            break
    if index < len(angle_list) - 1:
        index += 1
    else:
        index = 0

print(f'The answer to part 2 = {answer}')
