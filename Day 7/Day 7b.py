import itertools

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
    # print(f'Output = {output}')
    return pos, output


def op_5(prog, pos):
    change = False
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
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
    if val_1 != 0:
        pos = val_2
        change = True
    if not change:
        pos += 3  # Check --> This op only regards 2 values; should be +3 instead of +4?
    return pos


def op_6(prog, pos):
    change = False
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
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
    if val_1 == 0:
        pos = val_2
        change = True
    if not change:
        pos += 3  # Check --> This op only regards 2 values; should be +3 instead of +4?
    return pos


def op_7(prog, pos):
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
    if val_1 < val_2:
        prog[index_3] = 1
    else:
        prog[index_3] = 0
    pos += 4
    return pos


def op_8(prog, pos):
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
    if val_1 == val_2:
        prog[index_3] = 1
    else:
        prog[index_3] = 0
    pos += 4
    return pos



output = None

seq = [5, 6, 7, 8, 9]
sequences = list(itertools.permutations(seq))

max_output = 0

# Testcase
# sequences = [(4, 3, 2, 1, 0)]
# prog_org = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]



for sequence in sequences:
    progress = []
    for i in range(5):
        # Stores (program state, position, input_count)
        progress.append([prog.copy(), 0, 1])

    #Test
    print(len(progress[0]))


    input_val2 = 0
    pos = 0
    index_prog = 0
    finish = False
    while not finish:
        for phase in sequence:
            count_input = progress[index_prog][2]
            input_val1 = phase
            prog = progress[index_prog][0]
            pos = progress[index_prog][1]
            while True:
                if pos >= len(prog):
                    finish = True
                    break
                # print(f'Instruction {prog[pos]} at position {pos}, inputval 1 = {input_val1}')
                icode = prog[pos] % 100
                if icode == 1:
                    pos = op_1(prog, pos)
                elif icode == 2:
                    pos = op_2(prog, pos)
                elif icode == 3:
                    if count_input == 1:
                        pos = op_3(prog, pos, input_val1)
                        count_input += 1
                        progress[index_prog][2] = count_input
                    else:
                        pos = op_3(prog, pos, input_val2)
                elif icode == 4:
                    tup = op_4(prog, pos)
                    pos = tup[0]
                    output = tup[1]
                    # Store data and Start next program
                    progress[index_prog][0] = prog
                    progress[index_prog][1] = pos
                    input_val2 = output
                    if index_prog < 4:
                        index_prog += 1
                    else:
                        index_prog = 0
                    break
                elif icode == 5:
                    pos = op_5(prog, pos)
                elif icode == 6:
                    pos = op_6(prog, pos)
                elif icode == 7:
                    pos = op_7(prog, pos)
                elif icode == 8:
                    pos = op_8(prog, pos)
                elif icode == 99:
                    input_val2 = output
                    if index_prog == 4:
                        finish = True
                    if index_prog < 4:
                        index_prog += 1
                    else:
                        index_prog = 0
                    break
                else:
                    print('Danger! Danger! Unknown input command!!!')
                    break
            print(f'Sequence completed with output = {output}, output val 2 = {input_val2}')
    if output > max_output:
        max_output = output


print(f'The answer is {max_output}')