def highest(input: str) -> int:
    bank = [int(s) for s in input]


def test_puzzle():
    assert highest("987654321111111") == 98
    assert highest("811111111111119") == 89
    assert highest("234234234234278") == 78
    assert highest("818181911112111") == 92


def test_edge_cases():
    assert highest("918181911112111") == 98
    assert highest("898111111111111") == 98
