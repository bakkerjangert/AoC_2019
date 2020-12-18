def check_1():
    # Check is maximum is exceeded
    check = False
    number = int(''.join(map(str, value)))
    if number > int(end):
        check = True
    return check


def check_2():
    # Check if all numbers are increasing; in not it changes the input
    check = True
    for i in range(1, len(value)):
        if value[i] < value[i - 1]:
            value[i] = value[i - 1]
            check = False
            break
    return check


def check_3():
    check = False
    for i in range(1, len(value)):
        if value[i] == value[i - 1]:
            check = True
            break
    return check


def check_3b():
    check = False
    for i in range(1, len(value)):
        if value[i] == value[i - 1]:
            # end boundary
            if i == len(value) - 1 and value[i - 2] != value[i]:
                check = True
                break
            # start boundary
            elif i == 1 and value[i + 1] != value[i]:
                check = True
                break
            # middle part
            elif 1 < i < len(value) - 1:
                if value[i - 2] != value[i]:
                    if value[i + 1] != value[i]:
                        check = True
                        break
    return check


def add_number():
    number = int(''.join(map(str, value)))
    number += 1
    new_val = list()
    for char in str(number):
        new_val.append(int(char))
    return new_val

# It is a six-digit number
# No need to check
# The value is within the range given in your puzzle input
# --> Check 1
# Two adjacent digits are the same (like 22 in 122345)
# --> Check 3
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)
# --> Check 2


start = '356261'
end = '846303'

value = list()
for char in start:
    value.append(int(char))

counter = 0
counter_b = 0

iterations = 0

while True:
    iterations += 1
    if check_1():  # maximum range exceeded; stop
        break
    if not check_2():  # next number is generated continue to next iteration
        continue
    if check_3():  # check for 2 adjacent equal numbers
        counter += 1
    if check_3b():  # check for 2 adjacent equal numbers, but not 3
        counter_b += 1
    value = add_number()

print(f'The answer to part 1 is {counter} calculated in {iterations} iterations')
print(f'The answer to part 2 is {counter_b} calculated in {iterations} iterations')