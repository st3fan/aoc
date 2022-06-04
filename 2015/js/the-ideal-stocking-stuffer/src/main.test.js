import assert from 'assert';

import { part1, part2 } from './main.js';

describe('Exercise', function () {
    it('part 1 should be 254575', function () {
        assert.equal(part1(), 254575);
    });
    it('part 2 should be 1038736', function () {
        assert.equal(part2(), 1038736);
    });
});
