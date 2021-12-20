#!/usr/bin/env python3


import json


def add(a, b):
    return [a, b]


def split_number(n):
    if n % 2 == 0:
        return [n//2, n//2]
    return [n//2, n//2+1]


def reduce(l):
    return l


def load_data():
    return [json.loads(line) for line in open("day18.input").readlines()]


def part1():
    print(load_data())

# # If any pair is nested inside four pairs, the leftmost such pair explodes
#
# # To explode a pair, the pair's left value is added to the first regular number
# # to the left of the exploding pair (if any), and the pair's right value is added
# # to the first regular number to the right of the exploding pair (if any).
# # Exploding pairs will always consist of two regular numbers. Then, the entire
# # exploding pair is replaced with the regular number 0.
#
# def _find_exploding_pair(pair, parent=None, level=0):
#     print(f"Looking at {pair} at level {level}")
#
#     if isinstance(pair[0], int) and isinstance(pair[1], int) and level == 4:
#         print(f"We got to explode {pair} parent is {parent}")
#         if parent[0] == pair:
#             parent[0] = 0
#             parent[1] += pair[1] # walk up and find first parent with value on right
#         else:
#             parent[1] = 0
#             parent[0] += pair[0] # walk up and find first parent with value on left
#         return True
#
#     if isinstance(pair[0], list):
#         return _find_exploding_pair(pair[0], pair, level + 1)
#
#     if isinstance(pair[1], list):
#         return _find_exploding_pair(pair[1], pair, level + 1)
#
#     return False
#
#
# def find_first_right_number(node):
#     if isinstance(node.left, int):
#         return node
#     else:
#         if n := find_first_right_number(node.left):
#             return n
#     if isinstance(node.right, int):
#         return node
#     else:
#         if n := find_first_right_number(node.right):
#             return n
#
#
# def find_first_right_node(node):
#     node = node.parent
#     while node:
#         if isinstance(node.right, int):
#             return node
#         else:
#             if n := find_first_right_number(node):
#                 return n
#         node = node.parent
#
#
# def find_first_left_node(node):
#     node = node.parent
#     while node:
#         if isinstance(node.left, int):
#             return node
#         node = node.parent
#
#
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.level = None
        self.value = None


class NumberNode(Node):
    def __init__(self, parent: Node, value: int, level: int):
        super().__init__()
        self.parent = parent
        self.value = value
        self.level = level


def parse(pair, parent=None, level=0):
    node = Node()
    node.parent = parent
    node.level = level

    if isinstance(pair[0], int):
        node.left = NumberNode(node, pair[0], level+1)
    else:
        node.left = parse(pair[0], parent=node, level=level+1)

    if isinstance(pair[1], int):
        node.right = NumberNode(node, pair[1], level+1)
    else:
        node.right = parse(pair[1], parent=node, level=level+1)

    return node

#

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


def explode(node):
    #print(f"Looking at {node} at level {node.level} left={node.left} right={node.right} value={node.value}")

    # We are interested if this node is at level 4 and a final node (numbers left and right)
    if node.level == 4 and isinstance(node.left, NumberNode) and isinstance(node.right, NumberNode):

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
            node.parent.left = NumberNode(node.parent, 0, node.parent.right.level)
        elif node.parent.right == node:
            node.parent.right = NumberNode(node.parent, 0, node.parent.right.level)

        return True # Done!

    # Walk through the tree, left side
    if node.left and explode(node.left):
        return True

    # Welk through the tree, right side
    if node.right and explode(node.right):
        return True

    return False


def split(node):
    if isinstance(node, NumberNode) and node.value >= 10:
        pair = split_number(node.value)

        replacement = Node()
        replacement.parent = node.parent
        replacement.level = node.level
        replacement.left = NumberNode(replacement, pair[0], node.level)
        replacement.right = NumberNode(replacement, pair[1], node.level)

        if node.parent.left == node:
            node.parent.left = replacement
        elif node.parent.right == node:
            node.parent.right = replacement

        return True

    # Walk through the tree, left side
    if node.left and split(node.left):
        return True

    # Welk through the tree, right side
    if node.right and split(node.right):
        return True

    return False

if __name__ == "__main__":
    #walk(parse([7,[6,[5,[4,[3,2]]]]]))
    # t = parse([[[[0,7],4],[[7,8],[0,13]]],[1,1]])
    # walk(t)
    # if split(t):
    #     walk(t)

    a = parse([])
    b = parse([])

