import { assertEquals } from "https://deno.land/std@0.142.0/testing/asserts.ts";

import { part1, part2 } from './main.ts';

Deno.test("Day 1/1 - Not Quite Lisp", () => {
  assertEquals(part1(), 280);
});

Deno.test("Day 1/2 - Not Quite Lisp", () => {
  assertEquals(part2(), 1797);
});