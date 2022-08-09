
#include <stdio.h>

#define ROUND(ww, aa, bb, cc) \
    { \
        x = ((z % 26) / aa) + bb; \
        x = (x == ww) ? 0 : 1; \
        z *= (25*x)+1; \
        z += (ww+cc)*x; \
    }

int main() {
    for (int a = 1; a < 10; a++) {
        for (int b = 1; b < 10; b++) {
            for (int c = 1; c < 10; c++) {
                for (int d = 1; d < 10; d++) {
                    for (int e = 1; e < 10; e++) {
                        for (int f = 1; f < 10; f++) {
                            //printf("Progress %d %d %d %d %d %d\n", a, b, c, d, e, f);
                            for (int g = 1; g < 10; g++) {
                                for (int h = 1; h < 10; h++) {
                                    for (int i = 1; i < 10; i++) {
                                        for (int j = 1; j < 10; j++) {
                                            for (int k = 1; k < 10; k++) {
                                                for (int l = 1; l < 10; l++) {
                                                    for (int m = 1; m < 10; m++) {
                                                        for (int n = 1; n < 10; n++) {
                                                            int x = 0, y = 0, z = 0;

                                                            ROUND(a,  1,  13,  8); int y1 = y; int x1 = x; int z1 = z;
                                                            ROUND(b,  1,  12, 16); int y2 = y; int x2 = x; int z2 = z;
                                                            ROUND(c,  1,  10,  4); int y3 = y; int x3 = x; int z3 = z;
                                                            ROUND(d, 26, -11,  1); int y4 = y; int x4 = x; int z4 = z;
                                                            ROUND(e,  1,  14, 13); int y5 = y; int x5 = x; int z5 = z;
                                                            ROUND(f,  1,  13,  5); int y6 = y; int x6 = x; int z6 = z;
                                                            ROUND(g,  1,  12,  0); int y7 = y; int x7 = x; int z7 = z;
                                                            ROUND(h, 26,  -5, 10); int y8 = y; int x8 = x; int z8 = z;
                                                            ROUND(i,  1,  10,  7); int y9 = y; int x9 = x; int z9 = z;
                                                            ROUND(j, 26,   0,  2); int y10 = y; int x10 = x; int z10 = z;
                                                            ROUND(k, 26, -11, 13); int y11 = y; int x11 = x; int z11 = z;
                                                            ROUND(l, 26, -13, 15); int y12 = y; int x12 = x; int z12 = z;
                                                            ROUND(m, 26, -13, 14); int y13 = y; int x13 = x; int z13 = z;
                                                            ROUND(n, 26, -11,  9); int y14 = y; int x14 = x; int z14 = z;

                                                            if (z == 0) {
                                                                printf("Xxxxx %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n",
                                                                    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14);
                                                                printf("Yyyyy %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n",
                                                                    y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14);
                                                                printf("Zzzzz %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n",
                                                                    z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14);

                                                                printf("Valid %d %d %d %d %d %d %d %d %d %d %d %d %d %d\n",
                                                                    a, b, c, d, e, f, g, h, i, j, k, l, m, n);

                                                                //return 0;
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return 0;
}
