#!/usr/bin/env python3


import re
from dataclasses import dataclass


@dataclass
class Acceleration:
    x: int
    y: int
    z: int


@dataclass
class Velocity:
    x: int
    y: int
    z: int

    def __iadd__(self, other):
        if not isinstance(other, Acceleration):
            raise ValueError("other must be a Acceleration")
        return Velocity(self.x + other.x, self.y + other.y, self.z + other.z)


@dataclass
class Position:
    x: int
    y: int
    z: int

    def __iadd__(self, other):
        if not isinstance(other, Velocity):
            raise ValueError("other must be a Velocity")
        return Position(self.x + other.x, self.y + other.y, self.z + other.z)


@dataclass
class Particle:
    p: Position
    v: Velocity
    a: Acceleration

    def tick(self):
        self.v += self.a
        self.p += self.v

    def distance(self):
        return abs(self.p.x) + abs(self.p.y) + abs(self.p.z)


@dataclass
class Swarm:
    particles: [Particle]

    def tick(self):
        for p in self.particles:
            p.tick()


if __name__ == "__main__":

    particles = []
    for line in [line.strip() for line in open("day20.input").readlines()]:
        v = [int(m) for m in re.findall(r"-?\d+", line)]
        position = Position(v[0], v[1], v[2])
        velocity = Velocity(v[3], v[4], v[5])
        acceleration = Acceleration(v[6], v[5], v[6]) 
        particles.append(Particle(position, velocity, acceleration))

    swarm = Swarm(particles)
    
    for _ in range(5000):
        swarm.tick()

    distances = [p.distance() for p in swarm.particles]
    print(sorted(distances))
    
    min_num = min(distances)
    index = distances.index(min_num)

    print("Part one:", index)

