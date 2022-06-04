// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

import { crypto } from "https://deno.land/std@0.142.0/crypto/mod.ts";

const INPUT = 'bgvyzdsv'

function toHexString(bytes: ArrayBuffer): string {
    return new Uint8Array(bytes).reduce((str, byte) => str + byte.toString(16).padStart(2, "0"), "");
}

// This does not have to be async of course, but I thought that was an interesting
// exercise. The change in the tests was very minimal.

async function findPrefix(input: string, prefix: string): Promise<number> {
    for (let i = 1; i < Number.MAX_SAFE_INTEGER; i++) {
        const digest = toHexString(await crypto.subtle.digest("MD5", new TextEncoder().encode(`${input}${i}`)))
        if (digest.startsWith(prefix)) {
            return i;
        }
    }
    return 0;
}

async function part1(): Promise<number> {
    return await findPrefix(INPUT, '00000')
}

async function part2(): Promise<number> {
    return await findPrefix(INPUT, '000000')
}

export { part1, part2 };
