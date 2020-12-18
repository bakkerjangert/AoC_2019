with open('input.txt') as f:
    lines = f.read().splitlines()

relations = {}
planets = []
has_orbits = []

for line in lines:
    planet_1 = line.split(')')[0]
    planet_2 = line.split(')')[1]
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

sequeneces = []
for planet in planets:
    if has_orbits.count(planet) == 0:
        search_planet = planet
        sequence = []
        while search_planet != start_planet:
            sequence.append(search_planet)
            search_planet = relations[search_planet]
        sequence.append(search_planet)
        sequeneces.append(tuple(reversed(sequence)))

count = 0
for planet in planets:
    for line in sequeneces:
        if planet in line:
            count += line.index(planet)
            break

print(f'The answer is {count}')




