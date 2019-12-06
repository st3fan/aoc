#include <stdio.h>
#include <string.h>

int test_one(char *code) {
  while (*code != 0x00) {
    int count = 0;
    char c = *code;
    while (*code == c) {
      count++;
      code++;
    }
    if (count == 2) {
      return 1;
    }
  }
  return 0;
}

int test_two(char *code) {
  for (int i = 1; i <= 5; i++) {
    if (code[i] < code[i-1]) {
      return 0;
    }
  }
  return 1;
}

int main() {
  int count = 0;
  for (int i = 138307; i <= 654504; i++) {
    char code[7];
    sprintf(code, "%d", i);
    if (test_one(code) && test_two(code)) {
      count++;
    }
  }
  printf("%d\n", count);
  return 0;
}
