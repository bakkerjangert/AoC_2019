with open('input.txt') as f:
    lines = f.read().splitlines()

prog = list(map(int, lines[0].split(',')))


def op_1(prog, pos):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    val_1 = prog[index_1]
    val_2 = prog[index_2]
    prog[index_3] = val_1 + val_2


def op_2(prog, pos):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    val_1 = prog[index_1]
    val_2 = prog[index_2]
    prog[index_3] = val_1 * val_2


prog[1] = 12
prog[2] = 2

pos = 0

while True:
    icode = prog[pos]
    if icode == 1:
        op_1(prog, pos)
    elif icode == 2:
        op_2(prog, pos)
    elif icode == 99:
        print(f'The answer = {prog[0]}')
        exit()
    else:
        print('Danger! Danger! Unknown input command!!!')
        break
    pos += 4