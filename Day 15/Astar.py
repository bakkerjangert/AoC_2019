import numpy as np

# class Node(object):
#
#     def __init__(self, pos):
#         self.pos = pos
#         self.G = None
#         self.H = None
#         self.F = None
#         self.parent = None
#
#     def Set_F(self):
#         self.F = self.G + self.H
#
#     def Set_G(self):
#         self.G = self.parent.G + 1
#
#     def Set_H(self, end):
#         self.H = abs(self.pos[0] - end[0]) + abs(self.pos[1] - end[1])
#
#     def Set_parent(self, parent):
#         self.parent = parent
#
#     def __repr__(self):
#         string = f'Node at {self.pos} with value F({self.F}) = G({self.G}) + H({self.H})'
#         return string

def Astar(maze, start, end):
    # NP.ARRAY --> X, Y, F, H ---- Note --> G can be easily calculated and has no need to be stored
    x_max = len(maze[0]) - 1
    y_max = len(maze) - 1
    opened = np.zeros([1, 4], dtype=int)
    opened[0, 0] = start[0]
    opened[0, 1] = start[1]
    opened[0, 3] = opened[0, 2] + abs(end[0] - start[0]) + abs(end[1] - start[1])
    # closed = np.zeros([1, 4], dtype=int)
    closed = [-1, -1, -1, -1]
    cur_node = opened[0, :]
    iteration = 0
    while tuple(cur_node[0:2]) != end:
        iteration += 1
        print('\n\n' + '#' * 20)
        if len(opened) == 0:
            print('No open path left; solution is not found.')
            break
        # Sort opened list on H
        opened = opened[opened[:, -1].argsort()]

        # Select parent node and move it to closed list
        parent_node = opened[0, :].copy()
        print(f'\n--- Current iteration {iteration} with node {parent_node}')
        print(f'\n--- Printing Opened list ---\n{opened}')
        # closed += parent_node.copy()
        closed = np.vstack((closed, parent_node.copy()))
        opened = np.delete(opened, 0, 0)
        x = parent_node[0]
        y = parent_node[1]
        # child 1; above parent
        closed_x_y = closed[:, 0:2]
        closed_x_y = closed_x_y.tolist()
        opened_x_y = opened[:, 0:2]
        opened_x_y = opened_x_y.tolist()
        if y > 0:
            if maze[y - 1][x] == '.':
                child_x = x
                child_y = y - 1
                child_F = parent_node[2] + 1
                child_H = abs(child_x - end[0]) + abs(child_y - end[1]) + child_F
                if [child_x, child_y] in closed_x_y:
                    pass
                elif [child_x, child_y] in opened_x_y:
                    for i in range(len(opened)):
                        if opened[i][0] == child_x and opened[i][1] == child_y:
                            index_num = i
                            break
                    # index_num = np.where(np.all(opened[:, 0:2] == [child_x, child_y], axis=1))
                    print(f'Child 1 index = {index_num}')
                    if opened[index_num][3] > child_H:
                        opened[index_num][2] = child_F
                        opened[index_num][3] = child_H
                    else:
                        pass
                elif tuple([child_x, child_y]) == end:
                    # End found; break
                    break
                else:  # Node not in closed or opened list
                    data = [child_x, child_y, child_F, child_H]
                    # Add to opened
                    opened = np.vstack((opened, data))
                    # print(opened)
        # # child 2; left of parent
        if x > 0:
            if maze[y][x - 1] == '.':
                child_x = x - 1
                child_y = y
                child_F = parent_node[2] + 1
                child_H = abs(child_x - end[0]) + abs(child_y - end[1]) + child_F
                if [child_x, child_y] in closed_x_y:
                    pass
                elif [child_x, child_y] in opened_x_y:
                    for i in range(len(opened)):
                        if opened[i][0] == child_x and opened[i][1] == child_y:
                            index_num = i
                            break
                        # index_num = np.where(np.all(opened[:, 0:2] == [child_x, child_y], axis=1))
                    print(f'Child 1 index = {index_num}')
                    if opened[index_num][3] > child_H:
                        opened[index_num][2] = child_F
                        opened[index_num][3] = child_H
                    else:
                        pass
                elif tuple([child_x, child_y]) == end:
                    # End found; break
                    break
                else:  # Node not in closed or opened list
                    data = [child_x, child_y, child_F, child_H]
                    # Add to opened
                    opened = np.vstack((opened, data))
                    # print(opened)
        # # child 3; right of parent
        if x < x_max:
            if maze[y][x + 1] == '.':
                child_x = x + 1
                child_y = y
                child_F = parent_node[2] + 1
                child_H = abs(child_x - end[0]) + abs(child_y - end[1]) + child_F
                if [child_x, child_y] in closed_x_y:
                    pass
                elif [child_x, child_y] in opened_x_y:
                    for i in range(len(opened)):
                        if opened[i][0] == child_x and opened[i][1] == child_y:
                            index_num = i
                            break
                        # index_num = np.where(np.all(opened[:, 0:2] == [child_x, child_y], axis=1))
                    print(f'Child 1 index = {index_num}')
                    if opened[index_num][3] > child_H:
                        opened[index_num][2] = child_F
                        opened[index_num][3] = child_H
                    else:
                        pass
                elif tuple([child_x, child_y]) == end:
                    # End found; break
                    break
                else:  # Node not in closed or opened list
                    data = [child_x, child_y, child_F, child_H]
                    # Add to opened
                    opened = np.vstack((opened, data))
        # # Child 4; below parent
        if y < y_max:
            if maze[y + 1][x] == '.':
                child_x = x
                child_y = y + 1
                child_F = parent_node[2] + 1
                child_H = abs(child_x - end[0]) + abs(child_y - end[1]) + child_F
                if [child_x, child_y] in closed_x_y:
                    pass
                elif [child_x, child_y] in opened_x_y:
                    for i in range(len(opened)):
                        if opened[i][0] == child_x and opened[i][1] == child_y:
                            index_num = i
                            break
                        # index_num = np.where(np.all(opened[:, 0:2] == [child_x, child_y], axis=1))
                    print(f'Child 1 index = {index_num}')
                    if opened[index_num][3] > child_H:
                        opened[index_num][2] = child_F
                        opened[index_num][3] = child_H
                    else:
                        pass
                elif tuple([child_x, child_y]) == end:
                    # End found; break
                    break
                else:  # Node not in closed or opened list
                    data = [child_x, child_y, child_F, child_H]
                    # Add to opened
                    opened = np.vstack((opened, data))
        print(f'\n---Printing Closed list ---\n{closed}')

    # add last node
    data = [child_x, child_y, child_F, 0]
    closed = np.vstack((closed, data))
    print(f'\n--- Final Check on Closed list\n{closed}')
    path = gen_path(closed)
    path = path[::-1]
    return path # steps to end


def gen_path(closed_list):
    steps = closed_list[-1][2]
    # print(f'steps = {steps}')
    path = []
    # First add final point
    cur_x = closed_list[-1][0]
    cur_y = closed_list[-1][1]
    path.append((cur_x, cur_y))
    # print(path)
    for i in range(steps - 1, 0, -1):
        # print(i)
        for line in closed_list:
            if line[2] == i:
                if (line[0] == cur_x + 1 and line[1] == cur_y) or (line[0] == cur_x - 1 and line[1] == cur_y) or (line[0] == cur_x and line[1] == cur_y + 1) or (line[0] == cur_x and line[1] == cur_y - 1):
                    cur_x = line[0]
                    cur_y = line[1]
                    path.append((cur_x, cur_y))
                    break
    # print(path)
    return path



if __name__ == '__main__':
    maze = [['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]

    print(len(Astar(maze, (0, 0), (2, 2))))


