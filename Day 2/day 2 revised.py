with open('input.txt') as f:
    instruction = list(map(int, f.read().split(',')))

# Testing area
# instruction = [1, 0, 0, 0, 99]  # becomes [2, 0, 0, 0, 99] (1 + 1 = 2).
# instruction = [2, 3, 0, 3, 99]  # becomes [2, 3, 0, 6, 99] (3 * 2 = 6).
# instruction = [2, 4, 4, 5, 99, 0]  # becomes [2, 4, 4, 5, 99, 9801] (99 * 99 = 9801).
# instruction = [1, 1, 1, 4, 99, 5, 6, 0, 99]  # becomes [30, 1, 1, 4, 2, 5, 6, 0, 99].


def run_program(start_position):
    position = start_position
    while True:
        val = opcodes[instruction[position]][0](position)
        if val:
            break
        position += opcodes[instruction[position]][1]
    return instruction[0]


def opcode_1(cur_pos):
    val_1 = instruction[instruction[cur_pos + 1]]
    val_2 = instruction[instruction[cur_pos + 2]]
    instruction[instruction[cur_pos + 3]] = val_1 + val_2
    return False


def opcode_2(cur_pos):
    val_1 = instruction[instruction[cur_pos + 1]]
    val_2 = instruction[instruction[cur_pos + 2]]
    instruction[instruction[cur_pos + 3]] = val_1 * val_2
    return False


def opcode_99(hoax):
    return True


# Redirect to opcode; 2nd number is steps to increase
opcodes = {1: (opcode_1, 4),
           2: (opcode_2, 4),
           99: (opcode_99, 1)}

# set starting position
position = 0
program = instruction.copy()


# Part 1
# initiate 1202 program alarm
instruction[1] = 12
instruction[2] = 2

run_program(position)
print(f'The answer to part 1 = {instruction[0]}')

# Part 2
search_val = 19690720
found = False
answer = None

for noun in range(100):
    if found:
        break
    for verb in range(100):
        # reset program and initiate noun and verb
        instruction = program.copy()
        instruction[1] = noun
        instruction[2] = verb
        if run_program(position) == search_val:
            answer = 100 * noun + verb
            found = True
            break

print(f'The answer to part 2 = {answer}')
