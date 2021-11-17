#!/usr/bin/env python3

INPUT = [
    [2,  0, -2,  0, 3],
    [0,  5, -3,  0, 3],
    [0,  0,  5, -1, 8],
    [0, -1,  0,  5, 8]
]


#Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
#Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
#Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
#Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8


def main():
    for sprinkles in range(4,101):
        for butterscotch in range(sprinkles+1,101):
            for chocolate in range(sprinkles+butterscotch+1,101):
                for candy in range(sprinkles+butterscotch+chocolate+1),1010):
                        if sprinkles + butterscotch + chocolate + candy == 100:
                            print(sprinkles, butterscotch, chocolate, candy)


if __name__ == "__main__":
    main()
