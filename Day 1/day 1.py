with open('input.txt') as f:
    lines = f.read().splitlines()

answer = 0

for line in lines:
    answer += (int(line) // 3 - 2)

print(f'The answer = {answer}')