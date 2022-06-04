const { createHash } = await import('node:crypto');

const INPUT = 'bgvyzdsv';

function findPrefix(input, prefix) {
    for (let i = 1; i < Number.MAX_SAFE_INTEGER; i++) {
        const digest = createHash('md5').update(`${input}${i}`).digest('hex');
        if (digest.startsWith(prefix)) {
            return i;
        }
    }
    return undefined;
}

function part1() {
    return findPrefix(INPUT, '00000')
}

function part2() {
    return findPrefix(INPUT, '000000')
}


export { part1, part2 };