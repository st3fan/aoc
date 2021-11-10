#!/usr/bin/env python3


import re
from collections import defaultdict
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


@dataclass(frozen=True)
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
    i: int
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

    def remove_collisions(self):
        d = defaultdict(list)
        for p in self.particles:
            d[p.p].append(p)
        for particles in d.values():
            if len(particles) > 1:
                for p in particles:
                    self.particles.remove(p)


def read_particles(path):
    particles = []
    for i, line in enumerate([line.strip() for line in open(path).readlines()]):
        v = [int(m) for m in re.findall(r"-?\d+", line)]
        position = Position(v[0], v[1], v[2])
        velocity = Velocity(v[3], v[4], v[5])
        acceleration = Acceleration(v[6], v[7], v[8]) 
        particles.append(Particle(i, position, velocity, acceleration))
    return particles


if __name__ == "__main__":

    # Part 1

    particles = read_particles("day20.input")
    swarm = Swarm(particles)
    for _ in range(1000):
        swarm.tick()

    particles = sorted(swarm.particles, key=Particle.distance)

    print("Part one:", particles[0].i)

    # Part 2

    particles = read_particles("day20.input")
    swarm = Swarm(particles)
    for _ in range(1000):
        swarm.tick()
        swarm.remove_collisions()

    print("Part two:", len(swarm.particles))

