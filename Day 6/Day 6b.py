import time

start_time = time.time()

with open('input.txt') as f:
    lines = f.read().splitlines()

relations = {}
planets = []
has_orbits = []

for sequence in lines:
    planet_1 = sequence.split(')')[0]
    planet_2 = sequence.split(')')[1]
    if planet_2 in list(relations.keys()):
        print('HEY, ALREADY IN DICT KEYS')
    relations[planet_2] = planet_1
    for planet in (planet_1, planet_2):
        if planet not in planets:
            planets.append(planet)
    has_orbits.append(planet_1)

start_planet = None

for planet in planets:
    if planet not in list(relations.keys()):
        start_planet = planet
        print(f'Start planet = {start_planet}')

sequences = []
for planet in planets:
    if has_orbits.count(planet) == 0:
        search_planet = planet
        sequence = []
        while search_planet != start_planet:
            sequence.append(search_planet)
            search_planet = relations[search_planet]
        sequence.append(search_planet)
        sequences.append(tuple(reversed(sequence)))

count = 0
for planet in planets:
    for sequence in sequences:
        if planet in sequence:
            count += sequence.index(planet)
            break

print(f'The answer to part 1 is {count}')

start = 'YOU'
goal = 'SAN'
steps = 0

pos = start

while pos != goal:
    changed = False
    steps += 1
    for sequence in sequences:
        if pos in sequence and goal in sequence:
            index_pos = sequence.index(pos)
            pos = sequence[index_pos + 1]
            changed = True
            break
    if not changed:
        pos = relations[pos]

# Mind that steps is from YOU to SAN --> answer is 2 steps shorter
print(f'The answer to part 2 is {steps - 2}')

end_time = time.time()

print(f'Runtime is approx {end_time - start_time} seconds')


