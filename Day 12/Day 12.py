import re

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

for time in range(1000):
    print(f'\n--Time {time}---')
    for i in index:
        print(moons[i])
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
    states = []
    for i in index:
        moons[i].x += moons[i].vx
        moons[i].y += moons[i].vy
        moons[i].z += moons[i].vz

tot_en = 0

for moon in moons:
    pot_en = abs(moon.x) + abs(moon.y) + abs(moon.z)
    kin_en = abs(moon.vx) + abs(moon.vy) + abs(moon.vz)
    tot_en += pot_en * kin_en

print(f'The answer to Part 1 is {tot_en}')
