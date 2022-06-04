package main

import (
	"bufio"
	"errors"
	"os"
	"strconv"
	"strings"

	"golang.org/x/exp/constraints"
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

//

func Max[T constraints.Ordered](a, b T) T {
	if a > b {
		return a
	}
	return b
}

//

type Point struct {
	X int
	Y int
}

func NewPointFromString(s string) (Point, error) {
	components := strings.Split(s, ",")
	if len(components) != 2 {
		return Point{}, errors.New("invalid point")
	}

	x, err := strconv.Atoi(components[0])
	if err != nil {
		return Point{}, errors.New("invalid x")
	}

	y, err := strconv.Atoi(components[1])
	if err != nil {
		return Point{}, errors.New("invalid y")
	}

	return Point{x, y}, nil
}

//

type Grid[T comparable] struct {
	width  int
	height int
	points []T
}

func NewGrid[T comparable](width int, height int) *Grid[T] {
	return &Grid[T]{
		width:  width,
		height: height,
		points: make([]T, width*height),
	}
}

func (g *Grid[T]) Set(point Point, value T) {
	g.points[point.Y*g.width+point.X] = value
}

func (g *Grid[T]) Get(point Point) T {
	return g.points[point.Y*g.width+point.X]
}

func (g *Grid[T]) CountValues(v T) int {
	total := 0
	for i := range g.points {
		if g.points[i] == v {
			total += 1
		}
	}
	return total
}

func (g *Grid[T]) ReduceValues(f func(a, b T) T) T {
	acc := g.points[0]
	for i := range g.points[1:] {
		acc = f(acc, g.points[i])
	}
	return acc
}

//

type Operation int

const (
	Toggle  Operation = 0
	TurnOn  Operation = 1
	TurnOff Operation = 2
)

type Instruction struct {
	From Point
	To   Point
	Op   Operation
}

// turn off 370,39 through 425,839

func NewInstructionFromString(s string) (Instruction, error) {
	components := strings.Split(s, " ")

	from, err := NewPointFromString(components[len(components)-3])
	if err != nil {
		return Instruction{}, err
	}

	to, err := NewPointFromString(components[len(components)-1])
	if err != nil {
		return Instruction{}, err
	}

	switch components[len(components)-4] {
	case "on":
		return Instruction{From: from, To: to, Op: TurnOn}, nil
	case "off":
		return Instruction{From: from, To: to, Op: TurnOff}, nil
	case "toggle":
		return Instruction{From: from, To: to, Op: Toggle}, nil
	}

	return Instruction{}, errors.New("failed to parse instruction")
}

//

func part1(instructions []Instruction) int {
	grid := NewGrid[bool](1000, 1000)
	for _, i := range instructions {
		for y := i.From.Y; y <= i.To.Y; y++ {
			for x := i.From.X; x <= i.To.X; x++ {
				switch i.Op {
				case Toggle:
					grid.Set(Point{x, y}, !grid.Get(Point{x, y}))
				case TurnOn:
					grid.Set(Point{x, y}, true)
				case TurnOff:
					grid.Set(Point{x, y}, false)
				}
			}
		}
	}
	return grid.CountValues(true)
}

func part2(instructions []Instruction) int {
	grid := NewGrid[int](1000, 1000)
	for _, i := range instructions {
		for y := i.From.Y; y <= i.To.Y; y++ {
			for x := i.From.X; x <= i.To.X; x++ {
				switch i.Op {
				case Toggle:
					grid.Set(Point{x, y}, grid.Get(Point{x, y})+2)
				case TurnOn:
					grid.Set(Point{x, y}, grid.Get(Point{x, y})+1)
				case TurnOff:
					grid.Set(Point{x, y}, Max(0, grid.Get(Point{x, y})-1))
				}
			}
		}
	}
	return grid.ReduceValues(func(a, b int) int { return a + b })
}

func main() {
	input, err := readInputWithLineTransformer("input.txt", NewInstructionFromString)
	if err != nil {
		panic(err)
	}

	println("Part 1:", part1(input))
	println("Part 2:", part2(input))
}
