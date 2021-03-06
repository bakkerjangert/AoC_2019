with open('input.txt') as f:
    lines = f.read().splitlines()

prog = list(map(int, lines[0].split(',')))


def op_1(prog, pos):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        val_1 = prog[pos + 1]
    else:
        val_1 = prog[index_1]
    # Set val_2
    if code[1] == '1':
        val_2 = prog[pos + 2]
    else:
        val_2 = prog[index_2]
    prog[index_3] = val_1 + val_2
    pos += 4
    return pos


def op_2(prog, pos):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        val_1 = prog[pos + 1]
    else:
        val_1 = prog[index_1]
    if code[1] == '1':
        val_2 = prog[pos + 2]
    else:
        val_2 = prog[index_2]
    prog[index_3] = val_1 * val_2
    pos += 4
    return pos


def op_3(prog, pos, input_val):
    index_1 = prog[pos + 1]
    prog[index_1] = input_val
    pos += 2
    return pos


def op_4(prog, pos):
    index_1 = prog[pos + 1]
    code = str(prog[pos])
    while len(code) < 3:
        code = '0' + code
    if code[0] == '1':
        output = prog[pos + 1]
    else:
        output = prog[index_1]
    pos += 2
    print(f'Output = {output}')
    return pos, output


input_val = 1

output = None
pos = 0
while True:
    icode = prog[pos] % 100
    if icode == 1:
        pos = op_1(prog, pos)
    elif icode == 2:
        pos = op_2(prog, pos)
    elif icode == 3:
        pos = op_3(prog, pos, input_val)
    elif icode == 4:
        tup = op_4(prog, pos)
        pos = tup[0]
        output = tup[1]
    elif icode == 99:
        print(f'The answer = {output}')
        exit()
    else:
        print('Danger! Danger! Unknown input command!!!')
        break
