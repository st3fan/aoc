

from itertools import islice, product


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


def manhattan_distance(v):
    return abs(v[0]) + abs(v[1])


def around(p):
    for q in product([-1, 0, 1], repeat=2):
        if q != (0,0):
            yield (p[0] + q[0], p[1] + q[1])


def sort_str(s):
    return "".join(sorted(s))


def same(e):
    return len(set(e)) == 1


def empty(e):
    return len(e) == 0

