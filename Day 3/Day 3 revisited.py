with open('input.txt') as f:
    lines = f.read().splitlines()


def follow_path(instructions):
    point = [0, 0]
    path = set()
    for instruction in instructions:
        if instruction[0] == 'U':
            for i in range(int(instruction[1:])):
                point[1] += 1
                path.add(tuple(point))
        if instruction[0] == 'D':
            for i in range(int(instruction[1:])):
                point[1] -= 1
                path.add(tuple(point))
        if instruction[0] == 'R':
            for i in range(int(instruction[1:])):
                point[0] += 1
                path.add(tuple(point))
        if instruction[0] == 'L':
            for i in range(int(instruction[1:])):
                point[0] -= 1
                path.add(tuple(point))
    return path


def get_steps(instructions, intersections):
    point = [0, 0]
    step = 0
    steps = dict()
    for instruction in instructions:
        if instruction[0] == 'U':
            for i in range(int(instruction[1:])):
                step += 1
                point[1] += 1
                if tuple(point) in intersections and tuple(point) not in steps.keys():
                    steps[tuple(point)] = step
        if instruction[0] == 'D':
            for i in range(int(instruction[1:])):
                step += 1
                point[1] -= 1
                if tuple(point) in intersections and tuple(point) not in steps.keys():
                    steps[tuple(point)] = step
        if instruction[0] == 'R':
            for i in range(int(instruction[1:])):
                step += 1
                point[0] += 1
                if tuple(point) in intersections and tuple(point) not in steps.keys():
                    steps[tuple(point)] = step
        if instruction[0] == 'L':
            for i in range(int(instruction[1:])):
                step += 1
                point[0] -= 1
                if tuple(point) in intersections and tuple(point) not in steps.keys():
                    steps[tuple(point)] = step
    return steps


instruction_A = lines[0].split(',')
instruction_B = lines[1].split(',')
path_A = follow_path(instruction_A)
path_B = follow_path(instruction_B)

answer = 0
intersections = set()

for pos in path_A:
    if pos in path_B:
        val = abs(pos[0]) + abs(pos[1])
        # Input for part 2
        intersections.add(pos)
        # Part 1
        if (val < answer) or answer == 0:
            answer = val

print(f'The answer to part 1 = {answer} distance')

steps_A = get_steps(instruction_A, intersections)
steps_B = get_steps(instruction_B, intersections)

min_steps = 0

for point in intersections:
    local_steps = steps_A[point] + steps_B[point]
    if local_steps < min_steps or min_steps == 0:
        min_steps = local_steps

print(f'The answer to part 2 = {min_steps} steps')
