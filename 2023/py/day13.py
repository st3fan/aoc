#!/usr/bin/env python


from typing import List

from PIL import Image, ImageChops
from PIL.ImageStat import Stat


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def image_from_pattern(pattern: List[str]) -> Image.Image:
    image = Image.new("RGB", (len(pattern[0]), len(pattern)), WHITE)
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            if pattern[y][x] == '#':
                image.putpixel((x, y), BLACK)
    return image


def read_input() -> List[Image.Image]:
    with open("day13.txt") as f:
        patterns = f.read().strip().split("\n\n")
        return [image_from_pattern(pattern.split("\n")) for pattern in patterns]


def images_are_equal(a: Image, b: Image) -> bool:
  diff = ImageChops.difference(a, b)
  return not any(channel.getbbox() is not None for channel in diff.split())


def count_different_pixels(a: Image.Image, b: Image.Image) -> bool:
    stat = Stat(ImageChops.difference(a, b)).sum
    return stat[0] / 255


def find_mirror(image: Image.Image, flip=False) -> int|None:
    if flip:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    for x in range(1, image.width // 2 + 1):
        a = image.crop((0, 0, x, image.height))
        b = image.crop((x, 0, x+x, image.height)).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        if images_are_equal(a, b):
            return image.width - x if flip else x
    return None


# Like find_mirror except it now succeeds when there is 1 pixel difference.
def fuzz_mirror(image: Image.Image, flip=False) -> int|None:
    if flip:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    for x in range(1, image.width // 2 + 1):
        a = image.crop((0, 0, x, image.height))
        b = image.crop((x, 0, x+x, image.height)).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        if count_different_pixels(a, b) == 1:
            return image.width - x if flip else x
    return None


def part1() -> int:
    r = 0
    for image in read_input():
        # Vertical
        if n := find_mirror(image):
            r += n
        elif n := find_mirror(image, flip=True):
            r += n
        # Horizontal
        if n := find_mirror(image.transpose(Image.ROTATE_90)):
            r += n*100
        elif n := find_mirror(image.transpose(Image.ROTATE_90), flip=True):
            r += n*100
    return r


def part2() -> int:
    r = 0
    for image in read_input():
        # Vertical
        if n := fuzz_mirror(image):
            r += n
        elif n := fuzz_mirror(image, flip=True):
            r += n
        # Horizontal
        if n := fuzz_mirror(image.transpose(Image.ROTATE_90)):
            r += n*100
        elif n := fuzz_mirror(image.transpose(Image.ROTATE_90), flip=True):
            r += n*100
    return r

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
