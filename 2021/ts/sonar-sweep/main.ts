// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

function readAndMapInput<I>(path: string, f: (line: string, index: number) => I): Array<I> {
    const content = Deno.readTextFileSync(path);
    return content.trim().split('\n').map((line, index) => {
        return f(line, index);
    });
}

function readInput(path = './input.txt'): Array<number>  {
    return readAndMapInput(path, (line, _) => {
        return parseInt(line);
    });
}

export function part1(): number {
    const measurements = readInput();
    let n = 0;
    for (let i = 0; i < measurements.length-1; i++) {
        if (measurements[i] < measurements[i+1]) {
            n += 1;
        }
    }
    return n;
}

export function part2(): number {
    const measurements = readInput();
    let n = 0;
    for (let i = 0; i < measurements.length-3; i++) {
        const a = measurements[i+0] + measurements[i+1] + measurements[i+2];
        const b = measurements[i+1] + measurements[i+2] + measurements[i+3];
        if (a < b) {
            n += 1;
        }
    }
    return n;
}
