from day11 import apply_rules


def bench_split_number():
    assert apply_rules(123456) == [123, 456]


def test_split_number(benchmark):
    benchmark(bench_split_number)
