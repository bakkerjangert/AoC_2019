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

input_val = 2
rel_val = 0

output = None
pos = 0

prog[0] = 2

input_val_1 = 'A, B, A, C, B, A, C, B, A, C'
ass_1 = []
for char in input_val_1:
    if char != ' ':
        ass_1.append(ord(char))
ass_1.append(10)

input_val_2 = 'L, 6, L, 4, R, 6, 6'
ass_2 = []
for char in input_val_2:
    if char != ' ':
        ass_2.append(ord(char))
ass_2.append(10)

input_val_3 = 'L, 6, R, 6, 6, R, 6, 6, L, 8'
ass_3 = []
for char in input_val_3:
    if char != ' ':
        ass_3.append(ord(char))
ass_3.append(10)

input_val_4 = 'L, 6, L, 5, 5, L, 5, 5, L, 6'
ass_4 = []
for char in input_val_4:
    if char != ' ':
        ass_4.append(ord(char))
ass_4.append(10)

input_val_5 = 'y'
ass_5 = []
for char in input_val_5:
    if char != ' ':
        ass_5.append(ord(char))
ass_5.append(10)

ass = ass_1 + ass_2 + ass_3 + ass_4 + ass_5

board = [[]]
iteration = 0
while True:
    icode = prog[pos] % 100
    if icode == 1:
        pos = op_1(prog, pos, rel_val)
    elif icode == 2:
        pos = op_2(prog, pos, rel_val)
    elif icode == 3:
        # input_val = ass[iteration]
        print(f'Input iteration {iteration}')
        input_val = ass[iteration]
        iteration += 1
        pos = op_3(prog, pos, input_val, rel_val)
    elif icode == 4:
        tup = op_4(prog, pos, rel_val)
        pos = tup[0]
        output = tup[1]
        if output == 35:
            board[-1].append('#')
        elif output == 46:
            board[-1].append('.')
        elif output == 10:
            board.append([])
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

print(f'\nThe answer is {output}')

# Manually -->
# L, 6, L, 4, R, 12, L, 6, R, 12, R, 12, L, 8, L, 6, L, 4, R, 12, L, 6, L, 10, L, 10, L, 6, L, 6, R, 12, R, 12, L, 8,
# L, 6, L, 4, R, 12, L, 6, L, 10, L, 10, L, 6, L, 6, R, 12, R, 12, L, 8, L, 6, L, 4, R, 12, L, 6, L, 10, L, 10, L, 6
#
# A = L, 6, L, 4, R, 12
#
# A, L, 6, R, 12, R, 12, L, 8, A, L, 6, L, 10, L, 10, L, 6, L, 6, R, 12, R, 12, L, 8,
# A, L, 6, L, 10, L, 10, L, 6, L, 6, R, 12, R, 12, L, 8, A, L, 6, L, 10, L, 10, L, 6
#
# C = L, 6, L, 10, L, 10, L, 6
#
# A, L, 6, R, 12, R, 12, L, 8, A, C, L, 6, R, 12, R, 12, L, 8,
# A, C, L, 6, R, 12, R, 12, L, 8, A, C
#
# B = L, 6, R, 12, R, 12, L, 8
#
# A, B, A, C, B,
# A, C, B, A, C
