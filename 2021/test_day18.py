

from day18 import add, explode, split


def test_add():
    assert add([[[[4,3],4],4],[7,[[8,4],9]]], [1,1]) == [[[[[4,3],4],4],[7,[[8,4],9]]], [1,1]]
    assert add([1,2], [[3,4],5]) == [[1,2],[[3,4],5]]


def test_split():
    assert split(10) == [5,5]
    assert split(11) == [5,6]
    assert split(12) == [6,6]


def test_explode_returns():
    assert explode([[[[[9,8],1],2],3],4]) == True
    assert explode([[[[9,8],1],2],3]) == False


def test_explode():
    # (the 9 has no regular number to its left, so it is not added to any regular number).
    assert explode([[[[[9,8],1],2],3],4]) == [[[[0,9],2],3],4]
    # (the 2 has no regular number to its right, and so it is not added to any regular number).
    assert explode([7,[6,[5,[4,[3,2]]]]]) == [7,[6,[5,[7,0]]]]
    assert explode([[6,[5,[4,[3,2]]]],1]) == [[6,[5,[7,0]]],3]
    # (the pair [3,2] is unaffected because the pair [7,3] is further to the left; [3,2] would explode on the next action).
    assert explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
    assert explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[7,0]]]]
