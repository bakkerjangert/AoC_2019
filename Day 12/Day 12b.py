import re
from math import gcd

with open('input.txt') as f:
    lines = f.read().splitlines()

class Moon(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def __repr__(self):
        print(f'Moon at {self.x}, {self.y}, {self.z} with vel {self.vx}, {self.vy}, {self.vz}')
        return ''


moons = []

for line in lines:
    x = int(re.search(r'x=(.*?), y', line).group(1))
    y = int(re.search(r'y=(.*?), z', line).group(1))
    z = int(re.search(r'z=(.*?)>', line).group(1))
    moons.append(Moon(x, y, z))

index = [0, 1, 2, 3]

set_x = set(())
set_y = set(())
set_z = set(())

time_x = None
time_y = None
time_z = None
time = 0

while True:
    # Add current state to sets (Part 2)
    states_x = []
    states_y = []
    states_z = []
    for i in index:
        if time_x is None:
            states_x.append((moons[i].x, moons[i].vx))
        if time_y is None:
            states_y.append((moons[i].y, moons[i].vy))
        if time_z is None:
            states_z.append((moons[i].z, moons[i].vz))
    if time_x is None:
        cur_set_x = tuple(states_x)
        if cur_set_x in set_x:
            time_x = time
            print(f'\nTime x found at {time}')
        else:
            set_x.add(cur_set_x)
    if time_y is None:
        cur_set_y = tuple(states_y)
        if cur_set_y in set_y:
            time_y = time
            print(f'\nTime y found at {time}')
        else:
            set_y.add(cur_set_y)
    if time_z is None:
        cur_set_z = tuple(states_z)
        if cur_set_z in set_z:
            time_z = time
            print(f'\nTime z found at {time}')
        else:
            set_z.add(cur_set_z)
    # break if all times are found
    if time_x is not None and time_y is not None and time_z is not None:
        break

    # Continue calc from part 1
    time += 1
    # print(f'\n--Time {time}---')
    for i in index:
        # print(moons[i])
        index_left = index.copy()
        index_left.remove(i)
        for j in index_left:
            if moons[i].x < moons[j].x:
                moons[i].vx += 1
            elif moons[i].x > moons[j].x:
                moons[i].vx -= 1
            if moons[i].y < moons[j].y:
                moons[i].vy += 1
            elif moons[i].y > moons[j].y:
                moons[i].vy -= 1
            if moons[i].z < moons[j].z:
                moons[i].vz += 1
            elif moons[i].z > moons[j].z:
                moons[i].vz -= 1
    for i in index:
        moons[i].x += moons[i].vx
        moons[i].y += moons[i].vy
        moons[i].z += moons[i].vz

# Calculate lcm of x, y and z times --> Luckily state [0] is the initial state
times = [time_x, time_y, time_z]  # will work for an int array of any length
lcm = times[0]
for i in times[1:]:
    lcm = lcm * i // gcd(lcm, i)

print(f'\nAnswer = {lcm}')

