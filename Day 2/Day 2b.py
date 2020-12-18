with open('input.txt') as f:
    lines = f.read().splitlines()

prog = []

for line in lines:
    prog = line.split(',')
    # prog.append(int(line))

for i in range(len(prog)):
    prog[i] = int(prog[i])

prog_org = prog.copy()

for noun in range(100):
    for verb in range(100):
        prog = prog_org.copy()
        prog[1] = noun
        prog[2] = verb
        pos = 0
        while True:
            icode = prog[pos]
            index_1 = prog[pos + 1]
            index_2 = prog[pos + 2]
            index_3 = prog[pos + 3]
            val_1 = prog[index_1]
            val_2 = prog[index_2]
            if icode == 1:
                prog[index_3] = val_1 + val_2
            elif icode == 2:
                prog[index_3] = val_1 * val_2
            elif icode == 99:
                if prog[0] == 19690720:
                    print(f'The answer = {100*noun + verb}')
                    exit()
                break
            else:
                print('Danger! Danger! Unknown input command!!!')
                break
            pos += 4

print('Answer not found')
