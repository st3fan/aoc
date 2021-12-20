#!/usr/bin/env python3


import itertools
import functools
import json


def split_number(n):
    if n % 2 == 0:
        return [n//2, n//2]
    return [n//2, n//2+1]


def load_data():
    return [json.loads(line) for line in open("day18.input").readlines()]


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None


class NumberNode(Node):
    def __init__(self, parent: Node, value: int):
        super().__init__()
        self.parent = parent
        self.value = value


def parse(pair, parent=None):
    node = Node()
    node.parent = parent

    if isinstance(pair[0], int):
        node.left = NumberNode(node, pair[0])
    else:
        node.left = parse(pair[0], parent=node)

    if isinstance(pair[1], int):
        node.right = NumberNode(node, pair[1])
    else:
        node.right = parse(pair[1], parent=node)

    return node


# For debugging

def _walk(node):
    print("[", end="")
    if isinstance(node.left, NumberNode):
        print(node.left.value, end="")
    else:
        _walk(node.left)
    print(", ", end="")
    if isinstance(node.right, NumberNode):
        print(node.right.value, end="")
    else:
        _walk(node.right)
    print("]", end="")


def walk(node):
    _walk(node)
    print()


def find_right(node):
    if node.parent == None:
        return None
    if node == node.parent.right:
        return find_right(node.parent)
    n = node.parent.right
    while n.left != None:
        n = n.left
    return n


def find_left(node):
    if node.parent == None:
        return None
    if node == node.parent.left:
        return find_left(node.parent)
    n = node.parent.left
    while n.right != None:
        n = n.right
    return n


def explode(node, level=0):
    #print(f"Looking at {node} at level {node.level} left={node.left} right={node.right} value={node.value}")

    # We are interested if this node is at level 4 and a final node (numbers left and right)
    if level == 4 and isinstance(node.left, NumberNode) and isinstance(node.right, NumberNode):

        # the pair's left value is added to the first regular number to the
        # left of the exploding pair (if any), and the pair's right value is
        # added to the first regular number to the right of the exploding pair
        # (if any).

        if n := find_left(node):
            n.value += node.left.value
        if n:= find_right(node):
            n.value += node.right.value

        # Then, the entire exploding pair is replaced with the regular number 0.

        if node.parent.left == node:
            node.parent.left = NumberNode(node.parent, 0)
        elif node.parent.right == node:
            node.parent.right = NumberNode(node.parent, 0)

        return True

    # Walk through the tree, left side
    if node.left and explode(node.left, level+1):
        return True

    # Welk through the tree, right side
    if node.right and explode(node.right, level+1):
        return True

    return False


def split(node, level=0):
    if isinstance(node, NumberNode) and node.value >= 10:
        pair = split_number(node.value)

        replacement = Node()
        replacement.parent = node.parent
        replacement.left = NumberNode(replacement, pair[0])
        replacement.right = NumberNode(replacement, pair[1])

        if node.parent.left == node:
            node.parent.left = replacement
        elif node.parent.right == node:
            node.parent.right = replacement

        return True

    # Walk through the tree, left side
    if node.left and split(node.left, level+1):
        return True

    # Welk through the tree, right side
    if node.right and split(node.right, level+1):
        return True

    return False


def add(a, b):
    n = Node()
    n.left = a
    a.parent = n
    n.right = b
    b.parent = n
    return n


def _add(a, b):
    c = add(a, b)
    while explode(c) or split(c):
        pass
    return c


def _magnitude(node):
    if node.parent and isinstance(node.left, NumberNode) and isinstance(node.right, NumberNode):
        if node.parent.left == node:
            node.parent.left = NumberNode(node.parent, 3*node.left.value + 2*node.right.value)
        elif node.parent.right == node:
            node.parent.right = NumberNode(node.parent, 3*node.left.value + 2*node.right.value)
        return True

    # Walk through the tree, left side
    if node.left and _magnitude(node.left):
        return True

    # Welk through the tree, right side
    if node.right and _magnitude(node.right):
        return True

    return False


def magnitude(node):
    # This is pretty bad I'm sure there is a better way.
    while _magnitude(node):
        pass
    return 3*node.left.value + 2*node.right.value


def part1():
    r = functools.reduce(_add, [parse(n) for n in load_data()])
    return magnitude(r)


def part2():
    numbers = load_data()
    return max(magnitude(_add(parse(t[0]), parse(t[1]))) for t in itertools.permutations(numbers, 2))


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
