// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

function readAndMapInput<I>(path: string, f: (line: string, index: number) => I): Array<I> {
    const content = Deno.readTextFileSync(path);
    return content.trim().split('\n').map((line, index) => {
        return f(line, index);
    });
}

function readInput(path = './input.txt'): Array<string>  {
    return readAndMapInput(path, (line) => {
        return line;
    });
}

//

function _rate(l: Array<number>, reverse = false):  {
}

function gammaRate(input: Array<string>): number {
    return 0;
}

function epsilonRate(input: Array<string>): number {
    return 0;
}

function oxygenGeneratorRating(input: Array<string>): number {
    return 0;
}

function carbonDioxideScrubberRating(input: Array<string>): number {
    return 0;
}


//

export function part1(): number {
    const input = readInput();
    return gammaRate(input) * epsilonRate(input)
}

export function part2(): number {
    const input = readInput();
    return oxygenGeneratorRating(input) * carbonDioxideScrubberRating(input);
}
