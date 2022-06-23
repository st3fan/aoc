/*
 * Advent of Code 2021 Day 24
 *
 * Brute force solution that uses Darwin's Dispatch Queues. Only compiles
 * on macOS. Will use all available cores to split up the problem space.
 *
 * cc -Ofast day24.c && time ./a.out
 */

#include <stdio.h>
#include <dispatch/dispatch.h>

#include "day24.generated.c"

#define BLOCK_SIZE 43046721

void increment_inputs(uint64_t inputs[14]) {
  for (uint64_t i = 13; i >= 0; i--) {
    inputs[i]++;
    if (inputs[i] < 10) {
      return;
    }
    inputs[i] = 1;
  }
}

void print_inputs(char *prefix, uint64_t inputs[14]) {
  printf("%s:", prefix);
  for (uint64_t i = 0; i < 14; i++) {
    printf(" %llu", inputs[i]);
  }
  printf("\n");
}

void run_range(uint64_t d1, uint64_t d2, uint64_t d3, uint64_t d4, uint64_t d5, uint64_t d6) {
  uint64_t inputs[14];
  for (uint64_t n = 0; n < 14; n++) {
    inputs[n] = 1;
  }
  inputs[0] = d1;
  inputs[1] = d2;
  inputs[2] = d3;
  inputs[3] = d4;
  inputs[4] = d5;
  inputs[5] = d6;

  print_inputs("Working on range", inputs);

  for (uint64_t i = 0; i < BLOCK_SIZE; i++) {
    int z = execute_alu(inputs);
    if (z == 1) {
      print_inputs("Found matching inputs", inputs);
    }  
    increment_inputs(inputs);
  }
}

void part1() {
  dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
  dispatch_group_t group = dispatch_group_create();

  for (int i = 6; i <= 9; i++) {
    for (int j = 6; j <= 9; j++) {
      for (int k = 6; k <= 9; k++) {
        for (int l = 6; l <= 9; l++) {
          for (int m = 6; m <= 9; m++) {
            for (int n = 6; n <= 9; n++) {
              printf("Queueing group %d %d %d %d %d %d\n", i, j, k, l, m ,n);
              dispatch_group_async(group, queue, ^{
                run_range(i, j, k, l, m, n);
              });
            }
          }
        }
      }
    }
  }

  dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
  dispatch_release(group);
}

void foo() {
  uint64_t inputs[14];
  for (uint64_t n = 0; n < 14; n++) {
    inputs[n] = 1;
  }

  print_inputs("Test Start", inputs);

  for (uint64_t i = 0; i < 43046721; i++) {
    increment_inputs(inputs);
  }

  print_inputs("Test End", inputs);
}

int main() {
  //foo();
  part1();
  //part2();
  return 0;
}
