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

set_x = {}
set_y = {}
set_z = {}

time_x, time_y, time_z = None, None, None
time_x_0, time_y_0, time_z_0 = None, None, None
time = 0

print(f'\n---Initial state---')
for moon in index:
    print(moons[moon])

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
        if cur_set_x in set_x.keys():
            time_x = time
            time_x_0 = set_x[cur_set_x]
            print(f'\n--- Time x ---')
            for moon in index:
                print(moons[moon])
            print(f'\nTime x found at {time}, original time = {time_x_0}')
        else:
            set_x[cur_set_x] = time
    if time_y is None:
        cur_set_y = tuple(states_y)
        if cur_set_y in set_y.keys():
            time_y = time
            time_y_0 = set_y[cur_set_y]
            print(f'\n--- Time y ---')
            for moon in index:
                print(moons[moon])
            print(f'Time y found at {time}, original time = {time_y_0}')
        else:
            set_y[cur_set_y] = time
    if time_z is None:
        cur_set_z = tuple(states_z)
        if cur_set_z in set_z.keys():
            time_z = time
            time_z_0 = set_z[cur_set_z]
            print(f'\n--- Time z ---')
            for moon in index:
                print(moons[moon])
            print(f'\nTime z found at {time}, original time = {time_z_0}')
        else:
            set_z[cur_set_z] = time
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

if time_x_0 == time_y_0 == time_z_0 == 0:
    print('\nWhat a luck!!! time step [0] is the initial state of the universe!')

# Calculate lcm of x, y and z times --> Luckily state [0] is the initial state
times = [time_x, time_y, time_z]  # will work for an int array of any length
lcm = times[0]
for i in times[1:]:
    lcm = lcm * i // gcd(lcm, i)

print(f'\nThe universe repeats itself at time step {lcm}')
