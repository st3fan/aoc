// https://adventofcode.com/2015/day/1

package main

import "io/ioutil"

func readInput() (string, error) {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func part1(input string) int {
	floor := 0
	for _, c := range input {
		switch c {
		case '(':
			floor += 1
		case ')':
			floor -= 1
		}
	}
	return floor
}

func part2(input string) int {
	floor := 1
	for i, c := range input {
		switch c {
		case '(':
			floor += 1
		case ')':
			floor -= 1
		}
		if floor < 0 {
			return i
		}
	}
	return -1
}

func main() {
	input, err := readInput()
	if err != nil {
		panic(err)
	}

	println("Part 1", part1(input))
	println("Part 2", part2(input))
}
