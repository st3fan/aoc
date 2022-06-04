// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/

import { assertEquals } from "https://deno.land/std@0.142.0/testing/asserts.ts";

import { part1, part2 } from './main.ts';

Deno.test("Day 9/1 - All In A Single Night", () => {
  assertEquals(part1(), 141);
});

Deno.test("Day 9/2 - All In A Single Night", () => {
  assertEquals(part2(), 736);
});