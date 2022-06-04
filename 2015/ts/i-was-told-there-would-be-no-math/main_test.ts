import { assertEquals } from "https://deno.land/std@0.142.0/testing/asserts.ts";

import { part1, part2 } from './main.ts';

Deno.test("Day 4/1 - I was told there would be no math", () => {
  assertEquals(part1(), 1588178);
});

Deno.test("Day 4/2 - I was told there would be no math", () => {
  assertEquals(part2(), 3783758);
});