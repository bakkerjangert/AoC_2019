with open('input.txt') as f:
    instruction = list(map(int, f.read().split(',')))

# Test Area
instruction_1 = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]  #takes no input and produces a copy of itself as output.
instruction_2 = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]  # should output a 16-digit number.
instruction_3 = [104, 1125899906842624, 99]  # should output the large number in the middle.


class InitiateProgram(object):
    def __init__(self, code):
        self.code = dict()
        for i in range(len(code)):
            self.code[i] = code[i]
        self.input_values = None
        self.position = 0
        self.output = []
        self.instruction = None
        self.val = None
        self.opcodes = {'01': (self.opcode_1, 4),
                        '02': (self.opcode_2, 4),
                        '03': (self.opcode_3, 2),
                        '04': (self.opcode_4, 2),
                        '05': (self.opcode_5, 3),
                        '06': (self.opcode_6, 3),
                        '07': (self.opcode_7, 4),
                        '08': (self.opcode_8, 4),
                        '09': (self.opcode_9, 2),
                        '99': (self.opcode_99, 1)}
        self.code_99 = False
        self.relative_base = 0

    def run(self, input_values):
        self.input_values = input_values
        self.output.clear()
        while True:
            self.instruction = str(self.code[self.position])
            while len(self.instruction) < 5:
                self.instruction = '0' + self.instruction
            self.val = self.opcodes[self.instruction[-2:]][0]()
            if self.val is True:
                break
        return self.output

    def get_value(self, module, delta):
        if module == '0':
            try:
                val = self.code[self.code[self.position + delta]]
            except KeyError:
                val = 0
        elif module == '1':
            try:
                val = self.code[self.position + delta]
            except KeyError:
                val = 0
        elif module == '2':
            try:
                val = self.code[self.relative_base + self.code[self.position + delta]]
            except KeyError:
                val = 0
        else:
            val = None
            print(f'Invalid input! Program is terminated!')
            exit()
        return val

    def opcode_1(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        val_2 = self.get_value(self.instruction[-4], 2)
        write_index = self.code[self.position + 3]
        if self.instruction[-5] == '2':
            write_index += self.relative_base
        self.code[write_index] = val_1 + val_2
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_2(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        val_2 = self.get_value(self.instruction[-4], 2)
        write_index = self.code[self.position + 3]
        if self.instruction[-5] == '2':
            write_index += self.relative_base
        self.code[write_index] = val_1 * val_2
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_3(self):
        write_index = self.code[self.position + 1]
        if self.instruction[-3] == '2':
            write_index += self.relative_base
        self.code[write_index] = self.input_values.pop(0)
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_4(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        self.output.append(val_1)
        # print(f'The output = {val_1}')
        self.position += self.opcodes[self.instruction[-2:]][1]
        # Note: If False continues running, if True it halts after output
        if len(self.output) == 2:
            return True
        else:
            return False

    def opcode_5(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        val_2 = self.get_value(self.instruction[-4], 2)
        if val_1 != 0:
            self.position = val_2
        else:
            self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_6(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        val_2 = self.get_value(self.instruction[-4], 2)
        if val_1 == 0:
            self.position = val_2
        else:
            self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_7(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        val_2 = self.get_value(self.instruction[-4], 2)
        val_3 = 0
        if val_1 < val_2:
            val_3 += 1
        write_index = self.code[self.position + 3]
        if self.instruction[-5] == '2':
            write_index += self.relative_base
        self.code[write_index] = val_3
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_8(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        val_2 = self.get_value(self.instruction[-4], 2)
        val_3 = 0
        if val_1 == val_2:
            val_3 += 1
        write_index = self.code[self.position + 3]
        if self.instruction[-5] == '2':
            write_index += self.relative_base
        self.code[write_index] = val_3
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_9(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        self.relative_base += val_1
        # print(f'RB = {self.relative_base}')
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_99(self):
        self.code_99 = True
        return True


board = []
width = 100
height = 100

for y in range(height):
    board.append([])
    for x in range(width):
        board[-1].append('.')

bot_pos = [height // 2, width // 2]
tiles = set()
prog = InitiateProgram(instruction.copy())
directions = ['N', 'E', 'S', 'W']
bot_index = 0


while True:
    if board[bot_pos[1]][bot_pos[0]] == '.':
        input_val = [0]
    else:
        input_val = [1]
    outputs = prog.run(input_val)
    if len(outputs) == 0:
        # print(f'Program terminated with code 99')
        break
    # Paint
    tiles.add(tuple(bot_pos))
    if outputs[0] == 0:
        board[bot_pos[1]][bot_pos[0]] = '.'
    else:
        board[bot_pos[1]][bot_pos[0]] = '#'
    # Turn
    if outputs[1] == 0 and bot_index != 0:
        bot_index -= 1
    elif outputs[1] == 0:
        bot_index = 3
    elif outputs[1] == 1 and bot_index != 3:
        bot_index += 1
    else:
        bot_index = 0
    if directions[bot_index] == 'N':
        bot_pos[0] -= 1
    elif directions[bot_index] == 'E':
        bot_pos[1] += 1
    elif directions[bot_index] == 'S':
        bot_pos[0] += 1
    elif directions[bot_index] == 'W':
        bot_pos[1] -= 1

print(f'\nThe answer to part 1 = {len(tiles)}')

board.clear()
for y in range(height):
    board.append([])
    for x in range(width):
        board[-1].append('.')

bot_pos = [height // 2, width // 2]
tiles = set()
prog = InitiateProgram(instruction.copy())
directions = ['N', 'E', 'S', 'W']
bot_index = 3
board[bot_pos[1]][bot_pos[0]] = '#'

while True:
    if board[bot_pos[1]][bot_pos[0]] == '.':
        input_val = [0]
    else:
        input_val = [1]
    outputs = prog.run(input_val)
    if len(outputs) == 0:
        # print(f'Program terminated with code 99')
        break
    # Paint
    tiles.add(tuple(bot_pos))
    if outputs[0] == 0:
        board[bot_pos[1]][bot_pos[0]] = '.'
    else:
        board[bot_pos[1]][bot_pos[0]] = '#'
    # Turn
    if outputs[1] == 0 and bot_index != 0:
        bot_index -= 1
    elif outputs[1] == 0:
        bot_index = 3
    elif outputs[1] == 1 and bot_index != 3:
        bot_index += 1
    else:
        bot_index = 0
    if directions[bot_index] == 'N':
        bot_pos[0] -= 1
    elif directions[bot_index] == 'E':
        bot_pos[1] += 1
    elif directions[bot_index] == 'S':
        bot_pos[0] += 1
    elif directions[bot_index] == 'W':
        bot_pos[1] -= 1

message = []
for line in board:
    message.append('')
    for char in line:
        message[-1] += char
    if message[-1].count('#') == 0:
        del message[-1]
    if len(message) > 0:
        index = message[-1].index('#')
        message[-1] = message[-1][index:]
        message[-1] = message[-1][::-1]
        index = message[-1].index('#')
        message[-1] = message[-1][index:]
message[0] = '.' + message[0]

print(f'\nThe answer to part 2:\n')
for line in message:
    print(line)

