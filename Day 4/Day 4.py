start = 356261
stop = 846303

def check_code(string):
    double = False
    for i in range(len(string) - 1):
        if int(string[i + 1]) < int(string[i]):
            return False
        elif int(string[i]) == int(string[i + 1]):
            double = True
    if double:
        return True
    return False

count = 0
for i in range(start, stop):
    if check_code(str(i)):
        count += 1

print(f'The answer is {count}')
