#include <stdio.h>
#include <string.h>

int test_one(char *code) {
  for (char i = '0'; i <= '9'; i++) {
    for (int j = 0; j <= 4; j++) {
      if (code[j] == i && code[j+1] == i) {
	return 1;
      }
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

int test(int n) {
  char code[7];
  sprintf(code, "%d", n);

  if (test_one(code) == 0) {
    return 0;
  }

  if (test_two(code) == 0) {
    return 0;
  }
    
  return 1;
}

int main() {
  int count = 0;
  for (int i = 138307; i <= 654504; i++) {
    if (test(i)) {
      count += 1;
    }
  }
  printf("%d\n", count);
  return 0;
}
