type Dimensions = {
    length: number;
    width: number;
    height: number;
};

function readInput(path = './input.txt'): Array<Dimensions> {
    const content = Deno.readTextFileSync(path);
    return content.trim().split('\n').map(line => {
        const [length, width, height] = line.split('x').map(v => Number.parseInt(v));
        return {length, width, height};
    });
}

const paperNeeded = (d: Dimensions) => {
    const sides = [d.length * d.width, d.width * d.height, d.height * d.length];
    return 2*(sides[0] + sides[1] + sides[2]) + Math.min(...sides);
};

const ribbonNeeded = (d: Dimensions) => {
    const sides  = [d.length, d.width, d.height].sort((a, b) => a - b);
    return sides[0]*2 + sides[1]*2 + (d.length * d.width * d.height);
};

export function part1(): number {
    return readInput().map(d => paperNeeded(d)).reduce((a, b) => {return a+b}, 0);
}

export function part2(): number {
    return readInput().map(d => ribbonNeeded(d)).reduce((a, b) => {return a+b}, 0);
}