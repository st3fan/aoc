// Code in C, Code in C, Java's not the answer, Code in C.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *cache = NULL;

inline int get_next_number(int turn, int n) {
   int last_spoken = cache[n];
   if (last_spoken == -1) {
      return 0;
   } else {
      return turn - (last_spoken + 1);
   }
}

#define N 30000000

void nth_spoken_number() {
   cache = (int*) malloc(sizeof(int) * N);
   memset(cache, 0xff, sizeof(int) * N);

   cache[8] = 0;
   cache[0] = 1;
   cache[1] = 0;
   cache[17] = 2;
   cache[4] = 3;
   cache[1] = 4;

   int previous = 12;

   for (int turn = 6; turn < N; turn++) {
      int next = get_next_number(turn, previous);
      cache[previous] = turn-1;
      previous = next;
   }

   printf("answer = %d\n", previous);
}

int main() {
   nth_spoken_number();
}
