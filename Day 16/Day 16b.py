with open('input.txt') as f:
    lines = f.read().splitlines()

# Required sub_string after half of the string --> Determine from end; always use +1

string = lines[0]
offset = int(string[0:7])

rev_string = string[::-1]

tot_string = string * 10000
sub_string = tot_string[offset:]
rev_sub_string = sub_string[::-1]

data = []
for i in range(100):
    data.append(int(rev_sub_string[0]))

len_sub = len(sub_string)

rev_ans = ''

rev_ans += rev_sub_string[0]

# Note: Index 0 already initiated
for i in range(1, len(sub_string)):
    cur_data = [int(rev_sub_string[i])]
    for step in range(100):
        val = cur_data[step] + data[step]
        data[step] += cur_data[step]
        val = val % 10
        cur_data.append(val)
    rev_ans += str(cur_data[-1])
    data.append(cur_data.copy())
    cur_data.clear()
    print(f'Char {i} of {len_sub} finished --> at {round(i / len_sub * 100,2)}%')

ans = rev_ans[::-1]

print(f'The answer is {ans[0:8]}')
print(f'\n{ans[0:650]}')
print(ans)




