import itertools

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

def generate_list(total_inv, n):
    lst = itertools.combinations(total_inv, n)
    return list(lst)

input_val = -40  # Check wether to start with this or first command
rel_val = 0

output = None
output_lst = []
input_lst = ['north', 'south', 'east', 'west', 'take', 'drop', 'inv']
cur_input = []
inventory = []
pos = 0

route = [1, 4, 'weather machine', 0, 3, 1, 2, 4, 'whirled peas', 3, 1, 4, 'sand', 0, 4, 'festive hat', 0, 3, 0, 4,
         'space heater', 1, 2, 2, 2, 4, 'mug', 2, 1, 2, 1, 4, 'easter egg', 0, 3, 3, 1, 3, 4, 'shell', 1]
total_inv = ('weather machine', 'whirled peas', 'sand', 'festive hat', 'space heater', 'mug', 'easter egg', 'shell')
drop_lst = []
cur_drops = []
on_floor = []
n = 1
dropped = False
try_walk = False
checking = False
check_output = ''

while True:
    icode = prog[pos] % 100
    if icode == 1:
        pos = op_1(prog, pos, rel_val)
    elif icode == 2:
        pos = op_2(prog, pos, rel_val)
    elif icode == 3:
        input_val = cur_input[0]
        del cur_input[0]
        pos = op_3(prog, pos, input_val, rel_val)
    elif icode == 4:
        tup = op_4(prog, pos, rel_val)
        pos = tup[0]
        output = tup[1]
        if output == 10:
            # Generate output message
            string = ''
            for item in output_lst:
                string += chr(item)
            output_lst.clear()
            print(string)
            check_output += string
            # Get new input message
            if string == 'Command?':
                if len(route) == 0:
                    if len(drop_lst) == 0:
                        # generate next list to be dropped
                        drop_lst = generate_list(total_inv, n)
                        n += 1
                    if not dropped:
                        if len(cur_drops) == 0:
                            cur_drops = list(drop_lst[0])
                            del drop_lst[0]
                        cur_drop = cur_drops[0]
                        del cur_drops[0]
                        on_floor.append(cur_drop)
                        string = 'drop ' + cur_drop
                        for char in string:
                            cur_input.append(ord(char))
                        cur_input.append(10)
                        if len(cur_drops) == 0:
                            # all items dropped
                            dropped = True
                            try_walk = True
                            check_output = ''
                        continue
                    if try_walk:
                        # Try to walk with current weight
                        string = 'south'
                        for char in string:
                            cur_input.append(ord(char))
                        cur_input.append(10)
                        try_walk = False
                        checking = True
                        continue
                    if checking:
                        if '== Security Checkpoint ==' in check_output:
                            # Not correct value; continue
                            checking = False
                        else:
                            print('Exit found!')
                            break
                    # Otherwise pick up items from floor
                    if len(on_floor) > 0:
                        string = on_floor[0]
                        del on_floor[0]
                        string = 'take ' + string
                        for char in string:
                            cur_input.append(ord(char))
                        cur_input.append(10)
                        if len(on_floor) == 0:
                            dropped = False
                        continue
                else:
                    index = route[0]
                    cur_input = []
                    del route[0]
                for item in input_lst[index]:
                    cur_input.append(ord(item))
                if index == 4 or index == 5:
                    if len(route) == 0:
                        cur_item = input('Which item to take / drop?')
                    else:
                        cur_item = route[0]
                        del route[0]
                    cur_item = ' ' + cur_item
                    for char in cur_item:
                        cur_input.append(ord(char))
                cur_input.append(10)
        else:
            output_lst.append(output)
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