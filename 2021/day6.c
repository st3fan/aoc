#include <stdio.h>
#include <stdlib.h>

#define MAX_OUTPUT 1000000000000

int64_t part2(int64_t n) {
  int64_t *output = (int64_t*) malloc(MAX_OUTPUT * sizeof(int64_t));

  output[0] = n;
  output[1] = -1;

  for (int64_t i = 0; i < 256; i++) {
    //printf("Iteration %lld\n", i);

    int64_t *p = output;
    int64_t adding = 0;

    while (*p != -1) {
      if (*p == 0) {
        *p++ = 6;
        adding += 1;
      } else {
        *p++ -= 1;
      }
    }

    if (adding) {
      for (int64_t j = 0; j < adding; j++) {
        *p++ = 8;
      }
      *p = -1;
    }
  }

  int64_t total = 0;
  int64_t *p = output;
  while (*p++ != -1) {
    total++;
  }

  free(output);

  return total;
}

int main() {
  for (int64_t n = 1; n <= 5; n++) {
    printf("%lld: %lld\n", n, part2(n));
  }
}

