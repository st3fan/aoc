// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

import { assertEquals } from "https://deno.land/std@0.142.0/testing/asserts.ts";
import { part1, part2 } from './main.ts';

Deno.test("Day 1/1 - Dive!", () => {
  assertEquals(part1(), 1855814);
});

Deno.test("Day 1/2 - Dive!", () => {
  assertEquals(part2(), 1845455714);
});
