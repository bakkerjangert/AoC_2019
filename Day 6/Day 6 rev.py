with open('input.txt') as f:
    lines = f.read().splitlines()

list_1 = []
list_2 = []

for line in lines:
    list_1.append(line.split(')')[0])
    list_2.append(line.split(')')[1])

start_point = []
end_points = []
orbits = dict()

# First determine start point (only in list 1) and end points (only in list 2)
for i in range(len(list_1)):
    if list_1[i] not in list_2:
        start_point.append(list_1[i])
    if list_2[i] not in list_1:
        end_points.append(list_2[i])
    orbits[list_1[i]] = 0
    orbits[list_2[i]] = 0

# Now generate all possible paths, starting from the endpoints
paths = list()
for planet in end_points:
    paths.append([planet])
    index = list_2.index(planet)
    next_planet = list_1[index]
    while next_planet != start_point[0]:
        paths[-1].insert(0, next_planet)
        index = list_2.index(next_planet)
        next_planet = list_1[index]
    paths[-1].insert(0, next_planet)

# For each planet calculate the index in a path; the sum of those numbers is the answer
answer = 0
for key in orbits.keys():
    for line in paths:
        if key in line:
            orbits[key] = line.index(key)
            answer += line.index(key)
            break
        else:
            pass

print(f'The answer to part 1 = {answer}')

# Find a path with YOU and a path with SAN
path_YOU = None
path_SAN = None

for path in paths:
    if 'YOU' in path:
        path_YOU = path
    if 'SAN' in path:
        path_SAN = path
    if path_YOU is not None and path_SAN is not None:
        break

# Determine at which index the paths are common
i = 0
while True:
    if path_SAN[i] == path_YOU[i]:
        i += 1
    else:
        break

# Walk for YOU --> common point and then from common point --> SAN
steps = (path_YOU.index('YOU') - i) + (path_SAN.index('SAN') - i)
print(f'The answer to part 2 = {steps}')


