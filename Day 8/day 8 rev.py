with open('input.txt') as f:
    lines = f.read().splitlines()

message = lines[0]
width = 25
height = 6
pixels = width * height
layers = len(message) / pixels
zeros = 0
layer = None
decoded = list()
final_string = '2' * height * width

for i in range(int(layers)):
    string = message[i * pixels: (i + 1) * pixels]
    val = string.count('0')
    if val < zeros or zeros == 0:
        zeros = val
        layer = string
    decoded.append(string)
    for j in range(len(final_string)):
        if final_string[j] == '2':
            if j < len(final_string) - 1:
                final_string = final_string[:j] + string[j] + final_string[j + 1:]
            else:
                final_string = final_string[:j] + string[j]

print(f'The answer to part 1 is {layer.count("1")*layer.count("2")}\n')
print(f'The message to part 2 is the decoded image:\n')
for i in range(pixels):
    if final_string[i] == '1':
        print('#', end='')
    else:
        print(' ', end='')
    if (i + 1) % width == 0 and i != 0:
        print('')
