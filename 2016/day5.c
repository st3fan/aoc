/*
 * Advent of Code 2016, Day 5
 *
 * The Python version is not bad in terms of speed but I
 * wrote this straight C version to see how fast a basic
 * translation can go.
 *
 * Only compiles on Darwin as it requires CommonCrypto.
 * Just ignore the warning about MD5 being deprecated.
 *
 * This seems to be 2x faster than Python.
 */

#include <limits.h>
#include <stdio.h>
#include <string.h>

#include <CommonCrypto/CommonDigest.h>

#define INPUT "uqwqemis"

char *hex_chars = "0123456789abcdef";

void part1(char *door_id) {
  char result[9];

  int found = 0;
  for (int n = 0; n < INT_MAX; n++) {
    char tmp[256];
    sprintf(tmp, "%s%d", door_id, n);

    unsigned char digest[CC_MD5_DIGEST_LENGTH];
    CC_MD5(tmp, strlen(tmp), digest);

    if (digest[0] == 0 && digest[1] == 0 && (digest[2] & 0xf0) == 0) {
      result[found] = hex_chars[digest[2] & 0x0f];
      if (++found == 8) {
        break;
      }
    }
  }

  result[8] = 0;

  printf("Part one: %s\n", result);
}

void part2(char *door_id) {
  char result[9];
  memset(result, 0, 9);

  int found = 0;
  for (int n = 0; n < INT_MAX; n++) {
    char tmp[256];
    sprintf(tmp, "%s%d", door_id, n);

    unsigned char digest[CC_MD5_DIGEST_LENGTH];
    CC_MD5(tmp, strlen(tmp), digest);

    if (digest[0] == 0 && digest[1] == 0 && (digest[2] & 0xf0) == 0) {
      int position = digest[2] & 0x0f;
      if (position < 8 && result[position] == 0) {
        result[position] = hex_chars[(digest[3] & 0xf0) >> 4];
        if (++found == 8) {
          break;
        }
      }
    }
  }

  printf("Part two: %s\n", result);
}


int main() {
  part1(INPUT);
  part2(INPUT);
  return 0;
}

