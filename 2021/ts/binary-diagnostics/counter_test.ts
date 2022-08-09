// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

import { assertEquals } from "https://deno.land/std@0.142.0/testing/asserts.ts";
//import { Counter } from './counter.ts';

class Counter {
    private values: Map<unknown, number>;

    constructor(iterable: Iterable<unknown> | Map<unknown, number>) {
        this.values = new Map();

        if (iterable instanceof Map) {
            for (const [key, count] of iterable) {
                const n = this.values.get(key);
                if (n === undefined) {
                    this.values.set(key, count);
                } else {
                    this.values.set(key, n+count);
                }
            }
        } else {
            for (const key of iterable) {
                const n = this.values.get(key);
                if (n === undefined) {
                    this.values.set(key, 1);
                } else {
                    this.values.set(key, n+1);
                }
            }
        }
    }

    increment(key: unknown, i = 1) {
        const n = this.values.get(key);
        if (n === undefined) {
            this.values.set(key, i);
        } else {
            this.values.set(key, n+i);
        }
    }

    clear() {
        this.values.clear()
    }

    get total(): number {
        let sum = 0;
        for(const [_, e] of this.values) {
            sum += e;
        }
        return sum;
    }

    *elements(): Generator<unknown> {
        for (const [key, count] of this.values) {
            for (let i = 0; i < count; i++) {
                yield key;
            }
        }
    }
}

Deno.test("Create a counter from a Map", () => {
    let m = new Map<string, number>(Object.entries({a: 3, b: 2, c: 1}));
    let c = new Counter(m);
    assertEquals(c.total, 6);
});

Deno.test("Create a counter from an array", () => {
    let c = new Counter(['aa', 'aa', 'aa', 'bb', 'bb', 'cc']);
    assertEquals(c.total, 6);
});

Deno.test("Create a counter from a string", () => {
    let c = new Counter('aaabbc');
    assertEquals(c.total, 6);
});
