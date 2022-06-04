package main

import (
	"bufio"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"

	"golang.org/x/exp/constraints"
)

func Sum[T constraints.Ordered](values []T) T {
	var total T
	for _, v := range values {
		total += v
	}
	return total
}

func Min[T constraints.Ordered](values []T) T {
	min := values[0]
	for _, v := range values[1:] {
		if v < min {
			min = v
		}
	}
	return min
}

func MustParseInt(s string) int {
	value, err := strconv.Atoi(s)
	if err != nil {
		log.Fatalf("Failed to parse int <%s>: %s", s, err.Error())
	}
	return value
}

type Dimensions struct {
	length int
	width  int
	height int
}

func (d Dimensions) paperNeeded() int {
	sides := []int{d.length * d.width, d.width * d.height, d.height * d.length}
	return 2*Sum(sides) + Min(sides)
}

func (d Dimensions) ribbonNeeded() int {
	var sides sort.IntSlice = []int{d.length, d.width, d.height}
	sort.Sort(sides)
	return sides[0]*2 + sides[1]*2 + (d.length * d.width * d.height)
}

func NewDimensionsFromString(s string) (Dimensions, error) {
	lwh := strings.SplitN(s, "x", 3)
	return Dimensions{
		length: MustParseInt(lwh[0]),
		width:  MustParseInt(lwh[1]),
		height: MustParseInt(lwh[2]),
	}, nil
}

func readInput() ([]Dimensions, error) {
	file, err := os.Open("input.txt")
	if err != nil {
		return nil, err
	}

	defer file.Close()

	var dimensions []Dimensions

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		d, err := NewDimensionsFromString(scanner.Text())
		if err != nil {
			return nil, err
		}
		dimensions = append(dimensions, d)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return dimensions, nil
}

func part1(input []Dimensions) int {
	total := 0
	for _, d := range input {
		total += d.paperNeeded()
	}
	return total
}

func part2(input []Dimensions) int {
	total := 0
	for _, d := range input {
		total += d.ribbonNeeded()
	}
	return total
}

func main() {
	input, err := readInput()
	if err != nil {
		panic(err)
	}

	println("Part 1", part1(input))
	println("Part 2", part2(input))
}
