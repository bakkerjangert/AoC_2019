import time

start = time.time()

with open('input.txt') as f:
    lines = f.read().splitlines()

wire_1 = lines[0].split(',')
wire_2 = lines[1].split(',')

wire_1_co = [(0, 0)]
wire_2_co = [(0, 0)]

for line in wire_1:
    direction = line[0]
    steps = int(line[1:])
    if direction == 'R':
        for i in range(steps):
            wire_1_co.append((wire_1_co[-1][0] + 1, wire_1_co[-1][1]))
    elif direction == 'U':
        for i in range(steps):
            wire_1_co.append((wire_1_co[-1][0], wire_1_co[-1][1] + 1))
    elif direction == 'D':
        for i in range(steps):
            wire_1_co.append((wire_1_co[-1][0], wire_1_co[-1][1] - 1))
    elif direction == 'L':
        for i in range(steps):
            wire_1_co.append((wire_1_co[-1][0] - 1, wire_1_co[-1][1]))

wire_1_org = wire_1_co.copy()
wire_1_co = sorted(wire_1_co)
wire_1_x = []
wire_1_x_index = []

for i in range(len(wire_1_co)):
    x = wire_1_co[i][0]
    if x not in wire_1_x:
        wire_1_x.append(x)
        wire_1_x_index.append(i)
wire_1_x_index.append(len(wire_1_co))
print(wire_1_x)

# for line in wire_1_co:
#     print(line)

answer = 999999999999999999

for line in wire_2:
    direction = line[0]
    steps = int(line[1:])
    if direction == 'R':
        for i in range(steps):
            wire_2_co.append((wire_2_co[-1][0] + 1, wire_2_co[-1][1]))
            x = wire_2_co[-1][0]
            y = wire_2_co[-1][1]
            if x in wire_1_x:
                index_start = wire_1_x_index[wire_1_x.index(x)]
                index_end = wire_1_x_index[wire_1_x.index(x) + 1]
                for i in range(index_start, index_end):
                    if wire_1_co[i][1] == y:
                        time_section = wire_1_org.index((x, y)) + wire_2_co.index((x, y))
                        if time_section < answer:
                            answer = time_section
    elif direction == 'U':
        for i in range(steps):
            wire_2_co.append((wire_2_co[-1][0], wire_2_co[-1][1] + 1))
            x = wire_2_co[-1][0]
            y = wire_2_co[-1][1]
            if x in wire_1_x:
                index_start = wire_1_x_index[wire_1_x.index(x)]
                index_end = wire_1_x_index[wire_1_x.index(x) + 1]
                for i in range(index_start, index_end):
                    if wire_1_co[i][1] == y:
                        time_section = wire_1_org.index((x, y)) + wire_2_co.index((x, y))
                        if time_section < answer:
                            answer = time_section
    elif direction == 'D':
        for i in range(steps):
            wire_2_co.append((wire_2_co[-1][0], wire_2_co[-1][1] - 1))
            x = wire_2_co[-1][0]
            y = wire_2_co[-1][1]
            if x in wire_1_x:
                index_start = wire_1_x_index[wire_1_x.index(x)]
                index_end = wire_1_x_index[wire_1_x.index(x) + 1]
                for i in range(index_start, index_end):
                    if wire_1_co[i][1] == y:
                        time_section = wire_1_org.index((x, y)) + wire_2_co.index((x, y))
                        if time_section < answer:
                            answer = time_section
    elif direction == 'L':
        for i in range(steps):
            wire_2_co.append((wire_2_co[-1][0] - 1, wire_2_co[-1][1]))
            x = wire_2_co[-1][0]
            y = wire_2_co[-1][1]
            if x in wire_1_x:
                index_start = wire_1_x_index[wire_1_x.index(x)]
                index_end = wire_1_x_index[wire_1_x.index(x) + 1]
                for i in range(index_start, index_end):
                    if wire_1_co[i][1] == y:
                        time_section = wire_1_org.index((x, y)) + wire_2_co.index((x, y))
                        if time_section < answer:
                            answer = time_section
print(f'The answer is {answer}')

end = time.time()
print('--- Time for Self developed script ---')
print(end - start)
