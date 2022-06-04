enum ElevatorDirection {
    Up = "(",
    Down = ")"
}

function parseElevatorDirection(c: string): ElevatorDirection {
    switch (c) {
        case '(': return ElevatorDirection.Up;
        case ')': return ElevatorDirection.Down;
        default: throw new Error('unknown direction');
    }
}

function readInput(path = './input.txt'): Array<ElevatorDirection> {
    return Deno.readTextFileSync(path).trim().split('').map(c => {
        return parseElevatorDirection(c)
    });
}

export function part1(): number {
    let floor = 0;
    for (const c of readInput()) {
        switch (c) {
            case ElevatorDirection.Up:
                floor += 1;
                break;
            case ElevatorDirection.Down:
                floor -= 1;
                break;
        }
    }
    return floor;
}

export function part2(): number {
    let floor = 1;
    for (const [i, c] of readInput().entries()) {
        switch (c) {
            case ElevatorDirection.Up:
                floor += 1;
                break;
            case ElevatorDirection.Down:
                floor -= 1;
                break;
        }
        if (floor < 0) {
            return i;
        }
    }
    return -1;
}