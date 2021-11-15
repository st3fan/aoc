/*
 * Advent of Code 2015 Day 20
 *
 * Brute force solution that uses Darwin's Dispatch Queues. Only compiles
 * on macOS. Will use all available cores to split up the problem space.
 */

#include <stdio.h>
#include <dispatch/dispatch.h>

#define INPUT 33100000
#define NUM_HOUSES 10000000
#define BATCH_SIZE 50000

int number_of_presents(int house) {
  int n = 0;
  for (int elf = 1; elf <= house; elf++) {
    if ((house % elf) == 0) {
      n += (10 * elf);
    }
  }
  return n;
}

int main() {
  dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
  dispatch_group_t group = dispatch_group_create();

  __block int lowest_house = NUM_HOUSES;

  for (int i = 0; i < (NUM_HOUSES / BATCH_SIZE); i++) {
    dispatch_group_async(group, queue, ^{
      int start = i * BATCH_SIZE;
      for (int house = start; house <= start + BATCH_SIZE - 1; house++) {
        int n = number_of_presents(house);
        if (n >= INPUT) {
          dispatch_async(queue, ^{
            if (house < lowest_house) {
              lowest_house = house;
            }
          });
          return;
        }
      }
    });
  }

  dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
  dispatch_release(group);

  printf("Part one: %d\n", lowest_house);
}

