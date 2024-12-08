from day8 import Point, Vector


def test_point():
    p = Point(1, 2)
    assert p.x == 1
    assert p.y == 2


def test_substract_point():
    v = Point(2, 3) - Point(4, 0)
    assert v == Vector(-2, 3)


def test_add_vector():
    p = Point(0, 0) + Vector(5, 7)
    assert p == Point(5, 7)


def test_foo():
    a = Point(3, 5)
    b = Point(7, 11)

    v1 = a - b
    p1 = a + v1
    assert p1 == Point(-1, -1)

    v2 = b - a
    p2 = b + v2
    assert p2 == Point(11, 17)
