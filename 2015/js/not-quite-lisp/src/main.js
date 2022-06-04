const fs = require('fs');

const readInput = () => fs.readFileSync('src/input.txt', 'utf8').split('');

const part1 = () => {
    let floor = 0;
    for (const c of readInput()) {
        switch (c) {
            case '(':
                floor += 1;
                break;
            case ')':
                floor -= 1;
                break;
        }
    }
    return floor;
}

const part2 = () => {
    let floor = 1;
    for (const [i, c] of readInput().entries()) {
        switch (c) {
            case '(':
                floor += 1;
                break;
            case ')':
                floor -= 1;
                break;
        }
        if (floor < 0) {
            return i;
        }
    }
    return -1;
}

module.exports = { part1, part2 };
