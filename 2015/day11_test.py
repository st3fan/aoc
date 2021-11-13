

from day11 import has_unique_pairs, has_incrementing_triplet


def test_hash_unique_pairs():
    assert has_unique_pairs("foobar") == False
    assert has_unique_pairs("foobarr") == True
    assert has_unique_pairs("ooxaa") == True
    assert has_unique_pairs("baabaab") == False


def test_has_incrementing_triplet():
    assert has_incrementing_triplet("abc") == True
    assert has_incrementing_triplet("xabc") == True
    assert has_incrementing_triplet("abcx") == True

