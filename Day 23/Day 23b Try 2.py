from copy import deepcopy

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

class computer(object):
    def __init__(self, ID, prog):
        self.ID = ID
        self.prog = deepcopy(prog)
        self.pos = 0
        self.rel_val = 0
        self.input_vals = [ID]  # Start with input val ID; then add packages
        self.output = []
        self.received_data = False

    def run(self):
        if self.received_data:
            print(f'-- ID {self.ID} received data correctly --> {self.input_vals[-2:]}')
            self.received_data = False
        icode = self.prog[self.pos] % 100
        if icode == 1:
            self.pos = op_1(self.prog, self.pos, self.rel_val)
        elif icode == 2:
            self.pos = op_2(self.prog, self.pos, self.rel_val)
        elif icode == 3:
            if len(self.input_vals) != 0:
                input_val = self.input_vals[0]
                del self.input_vals[0]
            else:
                input_val = -1
            self.pos = op_3(self.prog, self.pos, input_val, self.rel_val)
        elif icode == 4:
            tup = op_4(self.prog, self.pos, self.rel_val)
            self.pos = tup[0]
            self.output.append(tup[1])
            if len(self.output) == 3:
                if self.output[0] == 255:
                    Y = self.output[2]
                    print(f'Answer found! Value {Y} send to memory 255 Y')
                    exit()
                else:
                    output_ID = self.output[0]
                    print(f'Computer ID {self.ID} writes data to ID {output_ID} --> {self.output[1:]}')
                    computers[self.output[0]].received_data = True
                    computers[self.output[0]].input_vals.append(self.output[1])
                    computers[self.output[0]].input_vals.append(self.output[2])
                    self.output.clear()
        elif icode == 5:
            self.pos = op_5(self.prog, self.pos, self.rel_val)
        elif icode == 6:
            self.pos = op_6(self.prog, self.pos, self.rel_val)
        elif icode == 7:
            self.pos = op_7(self.prog, self.pos, self.rel_val)
        elif icode == 8:
            self.pos = op_8(self.prog, self.pos, self.rel_val)
        elif icode == 9:
            tup = op_9(self.prog, self.pos, self.rel_val)
            self.pos = tup[0]
            self.rel_val = tup[1]
        elif icode == 99:
            print(f'End of Int Machine')
        else:
            print('Danger! Danger! Unknown input command!!!')


class NAT(object):
    def __init__(self):
        self.input_vals = [None, None]
        self.last_y = None

    def run(self):
        if self.last_y is not None:
            halted = 0
            for i in range(50):
                comp_ID = i
                print(f'Inputval ID {comp_ID} == {computers[comp_ID].input_val} and len input = {computers[comp_ID].input_vals}')
                if len(computers[comp_ID].input_vals) == 0 and computers[comp_ID].input_val == -1:
                    halted += 1

            if halted == 50:
                if self.input_vals[1] == self.last_y:
                    print(f'Answer found! First Y to be sent twice in a row = {self.last_y}')
                    exit()
                else:
                    self.last_y = self.input_vals[1]
                    computers[0].input_vals.append(self.input_vals[0])
                    computers[0].input_vals.append(self.input_vals[1])

input_val = 2
rel_val = 0

computers = {}

for i in range(50):
    computers[i] = computer(i, prog)

while True:
    for comp_ID in computers:
        # print(f'\n--- Running ID {comp_ID} ---')
        computers[comp_ID].run()

