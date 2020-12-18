from copy import deepcopy

with open('input.txt') as f:
    lines = f.read().splitlines()

data = {}
chemicals = {}
left_over = {}

for line in lines:
    k = line.split('=> ')[1]
    k = k.split()
    k[0] = int(k[0])
    chemicals[k[1]] = k[0]
    left_over[k[1]] = 0
    left_over['ORE'] = 0
    v = line.split(' =>')[0]
    v = v.split(', ')
    val = []
    for i in range(len(v)):
        val.append((int(v[i].split()[0]), v[i].split()[1]))
    data[tuple(k)] = tuple(val)

build = [(1, 'FUEL')]
iteration = 0
while True:
    iteration += 1
    print(f'\n----Iteration {iteration} -----')
    cur_build = build.copy()
    for item in cur_build:
        if item[1] == 'ORE':
            # No reaction needed
            continue
        chemical = item[1]
        req_number = item[0]
        number_produced = chemicals[chemical]
        factor = req_number / number_produced
        for j in data[(number_produced, chemical)]:
            chem = j[1]
            no = j[0] * factor
            build.append((no, chem))
        # remove from build
        build.remove(item)
        print(f'{item} --> {data[(number_produced, chemical)]}')
    # Check wether built only has ores
    print(build)
    print(list(left_over.values()))
    ores = True
    ores_per_fuel = 0
    for item in build:
        ores_per_fuel += item[0]
        if item[1] != 'ORE':
            ores = False
            break
    if ores:
        break

ore_limit = 1000000000000

fuel_total = int(ore_limit / ores_per_fuel)

print(f'The answer is {fuel_total} units of fuel')


