with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0]
index = 0

wide = 25
tall = 6

decoded = []

while index < len(string):
    if index % (wide * tall) == 0:
        decoded.append([])
    if index % wide == 0:
        decoded[-1].append([])
    decoded[-1][-1].append(string[index])
    index += 1

zero_min = 999999999
answer = 0

for part in decoded:
    zeros = 0
    ones = 0
    twos = 0
    for line in part:
        zeros += line.count('0')
        ones += line.count('1')
        twos += line.count('2')
    if zeros < zero_min:
        zero_min = zeros
        answer = ones * twos

print(f'The answer is {answer}')

message = []

for y in range(tall):
    message.append([])
    for x in range(wide):
        message[-1].append('2')

for line in message:
    print(line)

for lay in range(len(decoded)):
    for y in range(tall):
        for x in range(wide):
            if message[y][x] == '2':
                message[y][x] = decoded[lay][y][x]

print(f'\nThe message for part 2:\n')
for line in message:
    for char in line:
        if char == '1':
            print('#', end='')
        else:
            print(' ', end='')
    print('')

for y in range(tall):
    for x in range(wide):
        print(message[y][x], end=',')
    print('')
