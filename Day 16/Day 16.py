with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0]
# Test
# string = '12345678'


string_len = len(string)
factors = [0, 1, 0, -1]

for phase in range(100):
    new_str = ''
    n = 0
    for num in range(string_len):
        n += 1
        sub_string = '0' + string  #shift string to lef
        data = [sub_string[i:i + n] for i in range(0, len(sub_string), n)]
        index = 0
        cur_val = 0
        for item in data:
            if factors[index] != 0:
                cur_val += sum(map(int, list(item))) * factors[index]
            if index < 3:
                index += 1
            else:
                index = 0
        new_str += str(cur_val)[-1]
    string = new_str

print(string[0:8])




