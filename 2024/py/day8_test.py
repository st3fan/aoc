from day8 import Point, Vector, read_input, part1, part2


def test_point():
    p = Point(1, 2)
    assert p.x == 1
    assert p.y == 2


def test_vector():
    v = Vector(5, 7)
    assert v.x == 5
    assert v.y == 7


def test_substract_points():
    v = Point(2, 3) - Point(4, 0)
    assert v == Vector(-2, 3)


def test_add_vector():
    p = Point(0, 0) + Vector(5, 7)
    assert p == Point(5, 7)


def test_puzzle_logic():
    a = Point(3, 5)
    b = Point(7, 11)

    v1 = a - b
    p1 = a + v1
    assert p1 == Point(-1, -1)

    v2 = b - a
    p2 = b + v2
    assert p2 == Point(11, 17)


def bench_part1():
    width, height, antennas = read_input("day8.txt")
    assert part1(width, height, antennas) == 367


def bench_part2():
    width, height, antennas = read_input("day8.txt")
    assert part2(width, height, antennas) == 1285


def bench_both_parts():
    width, height, antennas = read_input("day8.txt")
    assert part1(width, height, antennas) == 367
    assert part2(width, height, antennas) == 1285


def test_part1_performance(benchmark):
    benchmark(bench_part1)


def test_part2_performance(benchmark):
    benchmark(bench_part2)


def test_both_parts_performance(benchmark):
    benchmark(bench_both_parts)
