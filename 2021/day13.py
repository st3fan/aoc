#!/usr/bin/env python3


from PIL import Image


def load_pixels():
    with open("day13.pixels") as fp:
        return [(int(x), int(y)) for x, y in (line.strip().split(",") for line in fp.readlines())]


def load_folds():
    with open("day13.folds") as fp:
        for line in (line.strip()[11:] for line in fp.readlines()):
            c = line.split("=")
            yield (c[0], int(c[1]))




def count_pixels(image):
    total = 0
    for x in range(image.width):
        for y in range(image.height):
            #print(image.getpixel((x,y)))
            if image.getpixel((x,y)) != (0,0,0,0):
                total += 1
    return total


# fold up ... b on top of a
# left, upper, right, lower


def fold_horizontally(image, y):
    print("o pixels:", count_pixels(image))

    a = image.transform((image.width, y), Image.EXTENT, (0, 0, image.width, y)).transpose(Image.FLIP_TOP_BOTTOM)
    print("a: box:", (0, 0, image.width-1, y-1))

    b = image.transform((image.width, image.height-y-1), Image.EXTENT, (0, y+1, image.width, image.height))
    print("b: box:", (0, y+1, image.width-1, image.height-1))

    print("a: size:", a.width, a.height)
    print("b: size:", b.width, b.height)

    print("a pixels:", count_pixels(a))
    print("b pixels:", count_pixels(b))

    assert b.height <= a.height

    a.alpha_composite(b, dest=(0, a.height-b.height))

    print("c pixels:", count_pixels(a))

    return a


def fold_vertically(image, x):
    a = image.transform((x, image.height), Image.EXTENT, (0, 0, x, image.height)).transpose(Image.FLIP_LEFT_RIGHT)
    b = image.transform((image.width-x-1, image.height), Image.EXTENT, (x+1, 0, image.width, image.height))
    assert b.width <= a.width
    a.alpha_composite(b, dest=(a.width-b.width, 0))
    return a

def part1():
    pixels = load_pixels()

    width = max(p[0] for p in pixels)+1
    height = max(p[1] for p in pixels)+1

    image = Image.new("RGBA", (width, height), color=(0,0,0,0))
    for p in pixels:
        image.putpixel(p, (255,0,0))

    for i, f in enumerate(load_folds()):
        match f:
            case ("x", int(x)):
                print(f"Folding vertically at {x}")
                image = fold_vertically(image, x)
            case ("y", int(y)):
                print(f"Folding horizontally at {y}")
                image = fold_horizontally(image, y)

        image.save(f"day13-{i}.png")
        print(f"After step {i}: {count_pixels(image)} pixels")

    return count_pixels(image)


if __name__ == "__main__":
    print("Part one:", part1(), "(Should be 17)")

