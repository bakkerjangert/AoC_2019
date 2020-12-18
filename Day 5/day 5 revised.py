with open('input.txt') as f:
    instruction = list(map(int, f.read().split(',')))

# # TEST AREA
# instruction = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006,
#                20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105,
#                1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]


def run_program():
    while True:
        cur_pos = position[0]
        code = str(instruction[cur_pos])
        while len(code) < 5:
            code = '0' + code
        val = opcodes[code[-2:]][0](cur_pos, code)
        if val is True:
            break
    return instruction[0]


def get_value(module, pos):
    if module == '0':
        val = instruction[instruction[pos]]
    elif module == '1':
        val = instruction[pos]
    else:
        val = None
        print(f'Invalid input! Program is terminated!')
        exit()
    return val


def opcode_1(cur_pos, code):
    val_1 = get_value(code[-3], cur_pos + 1)
    val_2 = get_value(code[-4], cur_pos + 2)
    instruction[instruction[cur_pos + 3]] = val_1 + val_2
    position[0] += opcodes[code[-2:]][1]
    return False


def opcode_2(cur_pos, code):
    val_1 = get_value(code[-3], cur_pos + 1)
    val_2 = get_value(code[-4], cur_pos + 2)
    instruction[instruction[cur_pos + 3]] = val_1 * val_2
    position[0] += opcodes[code[-2:]][1]
    return False


def opcode_3(cur_pos, code):
    instruction[instruction[cur_pos + 1]] = input_val
    position[0] += opcodes[code[-2:]][1]
    return False


def opcode_4(cur_pos, code):
    val_1 = get_value(code[-3], cur_pos + 1)
    output = val_1
    outputs.append(val_1)
    # print(f'The output = {output}')
    position[0] += opcodes[code[-2:]][1]
    return output


def opcode_5(cur_pos, code):
    val_1 = get_value(code[-3], cur_pos + 1)
    val_2 = get_value(code[-4], cur_pos + 2)
    if val_1 != 0:
        position[0] = val_2
    else:
        position[0] += opcodes[code[-2:]][1]
    return False


def opcode_6(cur_pos, code):
    val_1 = get_value(code[-3], cur_pos + 1)
    val_2 = get_value(code[-4], cur_pos + 2)
    if val_1 == 0:
        position[0] = val_2
    else:
        position[0] += opcodes[code[-2:]][1]
    return False


def opcode_7(cur_pos, code):
    val_1 = get_value(code[-3], cur_pos + 1)
    val_2 = get_value(code[-4], cur_pos + 2)
    val_3 = 0
    if val_1 < val_2:
        val_3 += 1
    instruction[instruction[cur_pos + 3]] = val_3
    position[0] += opcodes[code[-2:]][1]
    return False


def opcode_8(cur_pos, code):
    val_1 = get_value(code[-3], cur_pos + 1)
    val_2 = get_value(code[-4], cur_pos + 2)
    val_3 = 0
    if val_1 == val_2:
        val_3 += 1
    instruction[instruction[cur_pos + 3]] = val_3
    position[0] += opcodes[code[-2:]][1]
    return False


def opcode_99(hoax, code):
    return True


# Redirect to opcode; 2nd number is steps to increase
opcodes = {'01': (opcode_1, 4),
           '02': (opcode_2, 4),
           '03': (opcode_3, 2),
           '04': (opcode_4, 2),
           '05': (opcode_5, 3),
           '06': (opcode_6, 3),
           '07': (opcode_7, 4),
           '08': (opcode_8, 4),
           '99': (opcode_99, 1)}

# set starting position for Part 1
position = [0]
input_val = 1
outputs = []
program = instruction.copy()

run_program()

print(f'The answer to part 1 = {outputs[-1]}')

# set starting position for Part 2
position[0] = 0
input_val = 5
outputs = []
instruction = program.copy()
run_program()

print(f'The answer to part 2 = {outputs[-1]}')
