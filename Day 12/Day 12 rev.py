from math import gcd

class Moon(object):
    def __init__(self, coords):
        self.name = coords[3]
        self.strt_x, self.strt_y, self.strt_z = coords[0], coords[1], coords[2]
        self.pos_x, self.pos_y, self.pos_z = coords[0], coords[1], coords[2]
        self.vel_x, self.vel_y, self.vel_z = 0, 0, 0
        self.potential, self.kinetic, self.energy = None, None, None
        self.set_energy()

    def set_energy(self):
        self.potential = abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)
        self.kinetic = abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)
        self.energy = self.kinetic * self.potential

    def update_pos(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.pos_z += self.vel_z

    def check_repeat(self):
        x_y_z = []
        if self.pos_x == self.strt_x and self.vel_x == 0:
            x_y_z.append(True)
        else:
            x_y_z.append(False)
        if self.pos_y == self.strt_y and self.vel_y == 0:
            x_y_z.append(True)
        else:
            x_y_z.append(False)
        if self.pos_z == self.strt_z and self.vel_z == 0:
            x_y_z.append(True)
        else:
            x_y_z.append(False)
        return tuple(x_y_z)

    def __repr__(self):
        print(f'Moon {self.name}:')
        print(f'-- Position: {self.pos_x}, {self.pos_y}, {self.pos_z}')
        print(f'-- Velocity: {self.vel_x}, {self.vel_y}, {self.vel_z}')
        print(f'-- Energy: {self.kinetic} x {self.potential} = {self.energy}')
        return ''


moons = {'Io': Moon([-9, 10, -1, 'Io']),
         'Europa': Moon([-14, -8, 14, 'Europa']),
         'Ganymede': Moon([1, 5, 6, 'Ganymede']),
         'Callisto': Moon([-19, 7, 8, 'Callisto'])}

# Test
# moons = {'Io': Moon([-1, 0, 2, 'Io']),
#          'Europa': Moon([2, -10, -7, 'Europa']),
#          'Ganymede': Moon([4, -8, 8, 'Ganymede']),
#          'Callisto': Moon([3, 5, -1, 'Callisto'])}

moons_list = list(moons.keys())

found_x, found_y, found_z = False, False, False
restart = [None, None, None]
step = 0
positions = ('x', 'y', 'z')

while None in restart:
    # print(f'--- Timestep {step + 1} ---')
    # Update velocity; Note cannot update position yet, otherwise underlaying moons velocity are incorrect
    for moon_a in moons_list:
        for moon_b in moons_list:
            if moons[moon_a] != moons[moon_b]:
                if moons[moon_a].pos_x < moons[moon_b].pos_x:
                    moons[moon_a].vel_x += 1
                elif moons[moon_a].pos_x > moons[moon_b].pos_x:
                    moons[moon_a].vel_x -= 1
                if moons[moon_a].pos_y < moons[moon_b].pos_y:
                    moons[moon_a].vel_y += 1
                elif moons[moon_a].pos_y > moons[moon_b].pos_y:
                    moons[moon_a].vel_y -= 1
                if moons[moon_a].pos_z < moons[moon_b].pos_z:
                    moons[moon_a].vel_z += 1
                elif moons[moon_a].pos_z > moons[moon_b].pos_z:
                    moons[moon_a].vel_z -= 1
    # Update position + print positions
    Reset = [True, True, True]
    for moon in moons_list:
        moons[moon].update_pos()
        moons[moon].set_energy()
        var_tup = moons[moon].check_repeat()
        for i in range(3):
            if var_tup[i] is False:
                Reset[i] = False
        # print(moons[moon])
    for j in range(3):
        if Reset[j] is True and restart[j] is None:
            restart[j] = step + 1
            print(f'\nPostion {positions[j]} resets after {restart[j]} timesteps')
    # Answer part 1
    if step == 999:
        Total_energy = 0
        for moon in moons_list:
            Total_energy += moons[moon].energy
        print(f'The engery after 1000 steps = {Total_energy}')
    step += 1
    if None not in restart:
        break

lcm = restart[0]
for i in restart[1:]:
    lcm = lcm * i // gcd(lcm, i)

print(f'\nThe universe resets itself after lcm of x, y and z, which is at {lcm} time steps')
