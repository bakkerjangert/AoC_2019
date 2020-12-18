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