#!/usr/bin/env python3


import copy
import itertools


class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return "<Position %3d %3d %3d>" % (self.x, self.y, self.z)


class Velocity:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return "<Velocity %3d %3d %3d>" % (self.x, self.y, self.z)


class Moon:
    def __init__(self, name, position, velocity):
        self.name = name
        self.position = position
        self.velocity = velocity

    def __eq__(self, other):
        return self.name == other.name and self.position == other.position and self.velocity == other.velocity

    def potential_energy(self):
        return abs(self.position.x) + abs(self.position.y) + abs(self.position.z)

    def kinetic_energy(self):
        return abs(self.velocity.x) + abs(self.velocity.y) + abs(self.velocity.z)

    def energy(self):
        return self.potential_energy() * self.kinetic_energy()


class System:
    def __init__(self, moons):
        self.moons = moons
    
    def step(self, n=1):
        for i in range(n):
            self._step()

    def apply_gravity(self, a, b):
        if a.position.x > b.position.x:
            a.velocity.x -= 1
            b.velocity.x += 1
        elif a.position.x < b.position.x:
            a.velocity.x += 1
            b.velocity.x -= 1
            
        if a.position.y > b.position.y:
            a.velocity.y -= 1
            b.velocity.y += 1
        elif a.position.y < b.position.y:
            a.velocity.y += 1
            b.velocity.y -= 1
            
        if a.position.z > b.position.z:
            a.velocity.z -= 1
            b.velocity.z += 1
        elif a.position.z < b.position.z:
            a.velocity.z += 1
            b.velocity.z -= 1

    def apply_velocity(self, a):
        a.position.x += a.velocity.x
        a.position.y += a.velocity.y
        a.position.z += a.velocity.z
    
    def _step(self):
        for i, j in itertools.combinations(range(len(self.moons)), 2):
            self.apply_gravity(self.moons[i], self.moons[j])
        for i in range(len(self.moons)):
            self.apply_velocity(self.moons[i])

def one():
    moons = [
        Moon("Io", Position(1, 4, 4), Velocity(0, 0, 0)),
        Moon("Europa", Position(-4, -1, 19), Velocity(0, 0, 0)),
        Moon("Ganymede", Position(-15, -14, 12), Velocity(0, 0, 0)),
        Moon("Callisto", Position(-17, 1, 10), Velocity(0, 0, 0))
    ]    
    system = System(moons)
    system.step(1000)
    print("Day 12.1:", sum([moon.energy() for moon in system.moons]))


def two():
    moons1 = [
        Moon("Io",       Position(-1,   0,  2), Velocity(0, 0, 0)),
        Moon("Europa",   Position( 2, -10, -7), Velocity(0, 0, 0)),
        Moon("Ganymede", Position( 4,  -8,  8), Velocity(0, 0, 0)),
        Moon("Callisto", Position( 3,   5, -1), Velocity(0, 0, 0)),
    ]

    moons = [
        Moon("Io",       Position(-1,   0,  2), Velocity(0, 0, 0)),
        Moon("Europa",   Position( 2, -10, -7), Velocity(0, 0, 0)),
        Moon("Ganymede", Position( 4,  -8,  8), Velocity(0, 0, 0)),
        Moon("Callisto", Position( 3,   5, -1), Velocity(0, 0, 0)),
    ]
    
    system = System(moons)
    count = 0
    while True:
        count += 1
        system.step()

        if system.moons[0] == moons1[0] and system.moons[1] == moons1[1] and system.moons[2] == moons1[2] and system.moons[3] == moons1[3]:
            break

    print("Day 12.2:", count, "TODO This is incorrect")


if __name__ == "__main__":
    one()
    two()
