// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

import { pairwise, permutations, imap, min, max, sum } from "https://deno.land/x/itertools@v1.0.2/mod.ts";

function readAndTransformInput<I>(initial: I, f: (input: I, line: string) => I, path = './input.txt'): I {
    const content = Deno.readTextFileSync(path);
    return content.trim().split('\n').reduce((input, line) => {
        return f(input, line);
    }, initial);
}

type City = string;

type Input = {
    cities: Set<City>;
    distances: Map<string, number>;
}

function readInput(): Input {
    const initial = {cities: new Set<City>(), distances: new Map<string, number>()};
    return readAndTransformInput<Input>(initial, (input: Input, line: string): Input => {
        const [from, _to, to, _is, distance] = line.split(' ');
        input.cities.add(from).add(to);
        input.distances.set(`${from}:${to}`, parseInt(distance)).set(`${to}:${from}`, parseInt(distance));
        return input;
    });
}

function tripDistance(distances: Map<string, number>, trip: string[]): number {
    return sum(imap(pairwise(trip), ([from, to]) => {
        return distances.get(`${from}:${to}`) || 0;
    }));
}

export function part1(): number {
    const {cities, distances} = readInput();
    return min(imap(permutations(cities), (trip) => {
        return tripDistance(distances, trip);
    })) as number;
}

export function part2(): number {
    const {cities, distances} = readInput();
    return max(imap(permutations(cities), (trip) => {
        return tripDistance(distances, trip);
    })) as number;
}