import { readFileSync } from 'fs';

const readInput = () => {
    const content = readFileSync('src/input.txt', {encoding: 'utf8'});
    return content.trim().split('\n').map(line => {
        let [length, width, height] = line.split('x').map(v => Number.parseInt(v));
        return {length, width, height};
    });
}

const paperNeeded = (d) => {
    const a = 1;
    const sides = [d.length * d.width, d.width * d.height, d.height * d.length];
    return 2*(sides[0] + sides[1] + sides[2]) + Math.min(...sides);
};

const ribbonNeeded = (d) => {
    const sides  = [d.length, d.width, d.height].sort((a, b) => a - b);
    return sides[0]*2 + sides[1]*2 + (d.length * d.width * d.height);
};

const part1 = () => {
    return readInput().map(d => paperNeeded(d)).reduce((a, b) => {return a+b}, 0);
}

const part2 = () => {
    return readInput().map(d => ribbonNeeded(d)).reduce((a, b) => {return a+b}, 0);
}

export default { part1, part2 };

console.log(part1());
console.log(part2());
