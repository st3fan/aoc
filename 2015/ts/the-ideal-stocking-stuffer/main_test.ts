// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

import { assertEquals } from "https://deno.land/std@0.142.0/testing/asserts.ts";

import { part1, part2 } from './main.ts';

Deno.test("Day 4/1 - The Ideal Stocking Stuffer", async () => {
  assertEquals(await part1(), 254575);
});

Deno.test("Day 4/2 - The Ideal Stocking Stuffer", async () => {
  assertEquals(await part2(), 1038736);
});