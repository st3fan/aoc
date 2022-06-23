/* day24.c */

#include <stdint.h>
#include <stdio.h>

#include "day24.generated.c"

void print_inputs(uint64_t inputs[14]) {
  for (uint64_t i = 0; i < 14; i++) {
    printf("%llu ", inputs[i]);
  }
  printf("\n");
}

void part1() {
  uint64_t inputs[14];
  for (uint64_t i = 0; i < 14; i++) {
    inputs[i] = 1;
  }

  uint64_t n = 0;
  for (uint64_t i = 0; i < 22876792454961; i++) {
    n += 1;
    if (n % 1000000000 == 0) {
      printf("%llu\n", n);
    }
    int z = execute_alu(inputs);
    if (z == 1) {
      print_inputs(inputs);
    }
  }
}

int main() {
  part1();
  return 0;
}
