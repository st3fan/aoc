// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

function readAndMapInput<I>(path: string, f: (line: string, index: number) => I): Array<I> {
    const content = Deno.readTextFileSync(path);
    return content.trim().split('\n').map((line, index) => {
        return f(line, index);
    });
}

enum Direction {
    Forward = "forward",
    Down = "down",
    Up = "up",
}

interface Command {
    direction: Direction;
    units: number;
}

function readInput(path = './input.txt'): Array<Command>  {
    return readAndMapInput(path, (line) => {
        const [direction, units] = line.split(' ');
        switch (direction) {
            case 'forward':
                return { direction: Direction.Forward, units: parseInt(units) };
            case 'up':
                return { direction: Direction.Up, units: parseInt(units) };
            case 'down':
                return { direction: Direction.Down, units: parseInt(units) };
            default:
                throw Error(`Invalid input <${line}>`);
        }
    });
}

export function part1(): number {
    let position = 0;
    let depth = 0;
    for (const command of readInput()) {
        switch (command.direction) {
            case Direction.Forward:
                position += command.units;
                break;
            case Direction.Up:
                depth -= command.units;
                break;
            case Direction.Down:
                depth += command.units;
                break;
        }
    }
    return position * depth;
}

export function part2(): number {
    let position = 0;
    let depth = 0;
    let aim = 0;
    for (const command of readInput()) {
        switch (command.direction) {
            case Direction.Forward:
                position += command.units;
                depth += aim * command.units;
                break;
            case Direction.Up:
                aim -= command.units;
                break;
            case Direction.Down:
                aim += command.units;
                break;
        }
    }
    return position * depth;
}
