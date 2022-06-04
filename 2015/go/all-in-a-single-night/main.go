package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func readInputWithLineTransformer[T any](path string, f func(s string) (T, error)) ([]T, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}

	defer file.Close()

	var values []T

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		v, err := f(scanner.Text())
		if err != nil {
			return nil, err
		}
		values = append(values, v)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return values, nil
}

type Distance struct {
	From     string
	To       string
	Distance int
}

type Pair[A any, B any] struct {
	A A
	B B
}

type StringPair = Pair[string, string]

// London to Dublin = 464
func NewDistanceFromString(s string) (Distance, error) {
	components := strings.Split(s, " ")
	distance, err := strconv.Atoi(components[4])
	if err != nil {
		return Distance{}, nil
	}
	return Distance{
		From:     components[0],
		To:       components[2],
		Distance: distance,
	}, nil
}

func Permutations[T any](l []T) [][]T {
	return nil
}

func Pairwise[T any](l []T) []Pair[T, T] {
	var pairs []Pair[T, T]
	for i := 0; i < len(l); i++ {
		pairs = append(pairs, Pair[T, T]{l[i], l[i+1]})
	}
	return pairs
}

func part1(cities []string, distances map[StringPair]int) int {
	min := 0
	for _, trip := range Permutations(cities) {
		distance := 0
		for _, pair := range Pairwise(trip) {
			distance += distances[pair]
		}
		if distance < min {
			min = distance
		}
	}
	return min
}

func part2(cities []string, distances map[StringPair]int) int {
	return 0
}

func Contains[T comparable](values []T, element T) bool {
	for idx := range values {
		if values[idx] == element {
			return true
		}
	}
	return false
}

func CollectUniqueValues[I any, V comparable](input []I, f func(i I) []V) []V {
	var unique []V
	for idx := range input {
		for _, value := range f(input[idx]) {
			if !Contains(unique, value) {
				unique = append(unique, value)
			}
		}
	}
	return unique
}

func main() {
	input, err := readInputWithLineTransformer("input.txt", NewDistanceFromString)
	if err != nil {
		panic(err)
	}

	cities := CollectUniqueValues(input, func(d Distance) []string {
		return []string{d.From, d.To}
	})

	// TODO Maybe a BuildMap function?
	distances := map[StringPair]int{}
	for _, d := range input {
		distances[StringPair{d.From, d.To}] = d.Distance
		distances[StringPair{d.To, d.From}] = d.Distance
	}

	println("Part 1:", part1(cities, distances))
	println("Part 2:", part2(cities, distances))
}
