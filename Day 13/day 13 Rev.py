import os
import time

with open('input.txt') as f:
    instruction = list(map(int, f.read().split(',')))


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
        self.board = {}
        self.code_99 = False
        self.relative_base = 0
        self.symbols = ['.', '#', '=', '-', '0']
        self.pad_pos = None
        self.bal_pos = None
        self.score = None

    def run(self, input_values):
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
        if self.bal_pos < self.pad_pos:
            self.input_values = [-1]
        elif self.bal_pos > self.pad_pos:
            self.input_values = [1]
        else:
            self.input_values = [0]
        # print(f'Input value = {self.input_values}')
        write_index = self.code[self.position + 1]
        if self.instruction[-3] == '2':
            write_index += self.relative_base
        self.code[write_index] = self.input_values.pop(0)
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_4(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        # print(f'output value = {val_1}')
        self.output.append(val_1)
        if len(self.output) == 3:
            if self.output[0] == -1 and self.output[1] == 0:
                # print(f'Current score = {self.output[2]}')
                self.score = self.output[2]
                # self.print_screen()
            else:
                self.board[(self.output[0], self.output[1])] = self.symbols[self.output[2]]
            if self.output[0] != -1 and self.output[2] == 3:
                self.pad_pos = self.output[0]
            if self.output[0] != -1 and self.output[2] == 4:
                self.bal_pos = self.output[0]
            self.output = []
        self.position += self.opcodes[self.instruction[-2:]][1]
        # Note: If False continues running, if True it halts after output
        # if len(self.output) == 2:
        #     return True
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

    def print_screen(self):
        # print('\n'*100)
        print(f'\n\n----- Current Score = {self.score} -----')
        list1 = list(self.board.keys())
        list1.sort(key=lambda x: x[1])
        for xy in list1:
            if xy[0] == 0:
                print('')
            print(self.board[xy], end='')
        print('\n')
        time.sleep(0.2)
        return False

game = InitiateProgram(instruction)
board = game.run([0])
block_tiles = 0

for key in list(game.board.keys()):
    if game.board[key] == '=':
        block_tiles += 1
print(f'At start there are {block_tiles} block tiles present')


# Part 2
instruction[0] = 2
game = InitiateProgram(instruction)
board = game.run([0])

print(f'Total score after last blok = {game.score}')
