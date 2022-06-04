import assert from 'assert';

import { addTwo, addThree } from './add.js';

describe('Exercise', function () {
    it('part 1 should be 2', function () {
        assert.equal(addTwo(3), 5);
    });
    it('part 2 should be 2', function () {
        assert.equal(addThree(2), 5);
    });
});
