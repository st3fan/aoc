const fs = require('fs');

const readInput = () => {
    return fs.readFileSync('src/input.txt', {encoding: 'utf8'}).trim().split('');
}

class Point {
    constructor() {
        this.x = 0;
        this.y = 0;
    }
}

class InfiniteGrid {
    constructor() {
        this._points = new Map();
    }

    set(p, v) {
        this._points.set([p.x, p.y].toString(), v); // WHUAHAHAHAHAHA :-(
    }

    get(p) {
        return this._points.get([p.x, p.y].toString());
    }

    get length() {
        return this._points.size;
    }
}

class Santa {
    constructor() {
        this._position = new Point();
    }

    west() {
        this._position.x -= 1;
    }

    east() {
        this._position.x += 1;
    }

    north() {
        this._position.y -= 1;
    }

    south() {
        this._position.y += 1;
    }

    get position() {
        return this._position;
    }
}

function part1() {
    const grid = new InfiniteGrid();
    const santa = new Santa();

    for (const c of readInput()) {
        switch (c) {
            case '<':
                santa.west();
                break;
            case '>':
                santa.east();
                break;
            case '^':
                santa.north();
                break;
            case 'v':
                santa.south();
                break;
        }
        grid.set(santa.position, true);
    }

    return grid.length;
}

function part2() {
    const grid = new InfiniteGrid();
    const santas = [new Santa(), new Santa()];

    for (const [i, c] of readInput().entries()) {
        switch (c) {
            case '<':
                santas[i%2].west();
                break;
            case '>':
                santas[i%2].east();
                break;
            case '^':
                santas[i%2].north();
                break;
            case 'v':
                santas[i%2].south();
                break;
        }
        grid.set(santas[i%2].position, true);
    }

    return grid.length;
}

module.exports = { part1, part2 };

