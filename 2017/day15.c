/**
 * Silly brute force use all the memory kind of solution
 * that runs in milliseconds.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


#define FACTOR_A 16807
#define FACTOR_B 48271
#define START_A 873
#define START_B 583
#define MODULUS 2147483647

void part1() {
  uint64_t a = START_A;
  uint64_t b = START_B;

  int matches = 0;

  for (uint64_t i = 0; i < 40000000; i++) {
    a = (a * FACTOR_A) % MODULUS;
    b = (b * FACTOR_B) % MODULUS;

    if ((a & 0xffff) == (b & 0xffff)) {
      matches += 1;
    }
  }

  printf("Part one: %d\n", matches);
}

void part2() {
  uint64_t *found_a = malloc(5000000 * 8);
  uint64_t found_a_idx = 0;
  uint64_t *found_b = malloc(5000000 * 8);
  uint64_t found_b_idx = 0;

  uint64_t a = START_A;
  uint64_t b = START_B;

  while (1) {
    if (found_a_idx < 5000000) {
      a = (a * FACTOR_A) % MODULUS;
      if (a % 4 == 0) {
        found_a[found_a_idx++] = a;
      }
    }

    if (found_b_idx < 5000000) {
      b = (b * FACTOR_B) % MODULUS;
      if (b % 8 == 0) {
        found_b[found_b_idx++] = b;
      }
    }

    if (found_a_idx == 5000000 && found_b_idx == 5000000) {
      break;
    }
  }

  int matches = 0;

  for (int i = 0; i < 5000000; i++) {
    if ((found_a[i] & 0xffff) == (found_b[i] & 0xffff)) {
      matches += 1;
    }
  }

  printf("Part two: %d\n", matches);
}

int main(int argc, char **argv) {
  part1();
  part2();
}

