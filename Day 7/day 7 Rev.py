import itertools
with open('input.txt') as f:
    instruction = list(map(int, f.read().split(',')))


class InitiateProgram(object):
    def __init__(self, code):
        self.code = code
        self.input_values = None
        self.position = 0
        self.output = None
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
                        '99': (self.opcode_99, 1)}
        self.code_99 = False

    def run(self, input_values):
        self.input_values = input_values
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
            val = self.code[self.code[self.position + delta]]
        elif module == '1':
            val = self.code[self.position + delta]
        else:
            val = None
            print(f'Invalid input! Program is terminated!')
            exit()
        return val

    def opcode_1(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        val_2 = self.get_value(self.instruction[-4], 2)
        self.code[self.code[self.position + 3]] = val_1 + val_2
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_2(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        val_2 = self.get_value(self.instruction[-4], 2)
        self.code[self.code[self.position + 3]] = val_1 * val_2
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_3(self):
        self.code[self.code[self.position + 1]] = self.input_values.pop(0)
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_4(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        self.output = val_1
        # print(f'The output = {output}')
        self.position += self.opcodes[self.instruction[-2:]][1]
        # Note
        return True

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
        self.code[self.code[self.position + 3]] = val_3
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_8(self):
        val_1 = self.get_value(self.instruction[-3], 1)
        val_2 = self.get_value(self.instruction[-4], 2)
        val_3 = 0
        if val_1 == val_2:
            val_3 += 1
        self.code[self.code[self.position + 3]] = val_3
        self.position += self.opcodes[self.instruction[-2:]][1]
        return False

    def opcode_99(self):
        self.code_99 = True
        return True


# set starting position for Part 1
seq = [0, 1, 2, 3, 4]
sequences = list(itertools.permutations(seq))

max_thrust = 0
program = instruction.copy()

for sequence in sequences:
    input_val = [0]
    for booster in sequence:
        input_val.insert(0, booster)
        cur_prog = InitiateProgram(instruction.copy())
        thrust = cur_prog.run(input_val)
        input_val.append(thrust)
    if max_thrust < thrust:
        max_thrust = thrust

print(f'The answer to part 1 is {max_thrust}')

seq = [5, 6, 7, 8, 9]
sequences = list(itertools.permutations(seq))

for sequence in sequences:
    input_val = [0]
    code_99 = False
    boosters = list()
    for booster in range(5):
        boosters.append(InitiateProgram(instruction.copy()))
    first_run = True
    while code_99 is False:
        for i in range(5):
            # Sequence number only on first run!
            if first_run:
                input_val.insert(0, sequence[i])
            thrust = boosters[i].run(input_val)
            input_val.append(thrust)
            code_99 = boosters[i].code_99
        first_run = False
    if max_thrust < thrust:
        max_thrust = thrust

print(f'The answer to part 2 is {max_thrust}')