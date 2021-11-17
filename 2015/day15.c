/* Advent of Code - 2015 Day 16 */

#include <stdio.h>

int INPUT[4][5] = {
    {2,  0, -2,  0, 3}, /* Sprinkles */
    {0,  5, -3,  0, 3}, /* Butterscotch */
    {0,  0,  5, -1, 8}, /* Chocolate */
    {0, -1,  0,  5, 8}  /* Candy */
};

int score1(int a, int b, int c, int d) {
  int i1 = a*INPUT[0][0] + b*INPUT[1][0] + c*INPUT[2][0] + d*INPUT[3][0];
  int i2 = a*INPUT[0][1] + b*INPUT[1][1] + c*INPUT[2][1] + d*INPUT[3][1];
  int i3 = a*INPUT[0][2] + b*INPUT[1][2] + c*INPUT[2][2] + d*INPUT[3][2];
  int i4 = a*INPUT[0][3] + b*INPUT[1][3] + c*INPUT[2][3] + d*INPUT[3][3];

  if (i1 < 0) { i1 = 0; }
  if (i2 < 0) { i2 = 0; }
  if (i3 < 0) { i3 = 0; }
  if (i4 < 0) { i4 = 0; }

  return i1 * i2 * i3 * i4;
}

int score2(int a, int b, int c, int d) {
  int cal = a*INPUT[0][4] + b*INPUT[1][4] + c*INPUT[2][4] + d*INPUT[3][4];
  if (cal != 500) {
    return 0;
  }

  int i1 = a*INPUT[0][0] + b*INPUT[1][0] + c*INPUT[2][0] + d*INPUT[3][0];
  int i2 = a*INPUT[0][1] + b*INPUT[1][1] + c*INPUT[2][1] + d*INPUT[3][1];
  int i3 = a*INPUT[0][2] + b*INPUT[1][2] + c*INPUT[2][2] + d*INPUT[3][2];
  int i4 = a*INPUT[0][3] + b*INPUT[1][3] + c*INPUT[2][3] + d*INPUT[3][3];

  if (i1 < 0) { i1 = 0; }
  if (i2 < 0) { i2 = 0; }
  if (i3 < 0) { i3 = 0; }
  if (i4 < 0) { i4 = 0; }

  return i1 * i2 * i3 * i4;
}

void part1() {
  int best = 0;
  for (int a = 1; a <= 100; a++) {
    for (int b = 1; b <= 100; b++) {
      for (int c = 1; c <= 100; c++) {
        for (int d = 1; d <= 100; d++) {
          if (a+b+c+d == 100) {
            int s = score1(a, b ,c ,d);
            if (s > best) {
              best = s;
            }
          }
        }
      }
    }
  }
  printf("Part one: %d\n", best);
}

void part2() {
  int best = 0;
  for (int a = 1; a <= 100; a++) {
    for (int b = 1; b <= 100; b++) {
      for (int c = 1; c <= 100; c++) {
        for (int d = 1; d <= 100; d++) {
          if (a+b+c+d == 100) {
            int s = score2(a, b ,c ,d);
            if (s > best) {
              best = s;
            }
          }
        }
      }
    }
  }
  printf("Part two: %d\n", best);
}


int main() {
  part1();
  part2();
  return 0;
}
