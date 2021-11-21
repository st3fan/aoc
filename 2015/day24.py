from functools import reduce
from itertools import combinations
from operator import mul


INPUT = [1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]


def quantum_entanglement(packages, num_groups):
	target_weight = sum(INPUT) // num_groups
	for i in range(len(INPUT)):
		q = [reduce(mul, c) for c in combinations(packages, i) if sum(c) == target_weight]
		if q:
			return min(q)

if __name__ == "__main__":
	print("Part one:", quantum_entanglement(INPUT, 3))
	print("Part two:", quantum_entanglement(INPUT, 4))

