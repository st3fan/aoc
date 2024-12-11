// Brute forcing part 1 is fast but of course this will not work on part 2.

#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


#define N 75000


int calculate(uint64_t *a, uint64_t *b, uint64_t number, int rounds) {
    for (int i = 0; i < N; i++) {
        a[i] = UINT64_MAX;
        b[i] = UINT64_MAX;
    }

    uint64_t *src = a;
    uint64_t *dst = b;

    src[0] = number;

    for (int i = 0; i < rounds; i++) {
        printf("Round %d\n", i+1);

        uint64_t *p = src;
        uint64_t *q = dst;

        while (*p != UINT64_MAX) {
            if (*p == 0) {
                *q++ = 1;
                p++;
                continue;
            }

            int num_digits = (int)log10(*p) + 1;
            if ((num_digits & 1) == 0) {
                int split_factor = pow(10, num_digits / 2);
                *q++ = *p / split_factor;
                *q++ = *p % split_factor;
                p++;
                continue;
            }

            *q++ = (*p++ * 2024);
        }

        // Swap the buffers
        uint64_t *tmp = src;
        src = dst;
        dst = tmp;
    }

    int total_stones = 0;

    uint64_t *p = src;
    while (*p++ != UINT64_MAX) {
        total_stones += 1;
    }

    return total_stones;
}

int main() {
    int rounds = 25;

    uint64_t *a = malloc(N * sizeof(uint64_t));
    uint64_t *b = malloc(N * sizeof(uint64_t));

    int total_stones = 0;
    total_stones += calculate(a, b, 92, rounds);
    total_stones += calculate(a, b, 0, rounds);
    total_stones += calculate(a, b, 286041, rounds);
    total_stones += calculate(a, b, 8034, rounds);
    total_stones += calculate(a, b, 34394, rounds);
    total_stones += calculate(a, b, 795, rounds);
    total_stones += calculate(a, b, 8, rounds);
    total_stones += calculate(a, b, 2051489, rounds);

    printf("Part1: %d\n", total_stones);
}
