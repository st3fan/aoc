package main

import "io/ioutil"

type Move rune

const (
	North Move = '^'
	South Move = 'v'
	East  Move = '>'
	West  Move = '<'
)

//

type Point struct {
	X int
	Y int
}

//

type InfiniteGrid[T any] struct {
	nodes map[Point]T
}

func NewInfiniteGrid[T any]() *InfiniteGrid[T] {
	return &InfiniteGrid[T]{
		nodes: map[Point]T{},
	}
}

func (g *InfiniteGrid[T]) Set(position Point, value T) {
	g.nodes[position] = value
}

func (g *InfiniteGrid[T]) Get(position Point) (T, bool) {
	value, ok := g.nodes[position]
	return value, ok
}

func (g *InfiniteGrid[T]) Len() int {
	return len(g.nodes)
}

//

type Santa struct {
	Position Point
}

func NewSanta() *Santa {
	return &Santa{
		Position: Point{0, 0}, // Not needed but for clarity
	}
}

func (s *Santa) MoveNorth() {
	s.Position.Y -= 1
}

func (s *Santa) MoveSouth() {
	s.Position.Y += 1
}

func (s *Santa) MoveWest() {
	s.Position.X -= 1
}

func (s *Santa) MoveEast() {
	s.Position.X += 1
}

//

func readInput() ([]Move, error) {
	data, err := ioutil.ReadFile("input.txt")
	if err != nil {
		return nil, err
	}

	var moves []Move
	for _, v := range data { // This looks weird
		moves = append(moves, Move(v))
	}

	return moves, nil
}

func part1(moves []Move) int {
	grid := NewInfiniteGrid[bool]()
	santa := NewSanta()

	for _, move := range moves {
		switch move {
		case North:
			santa.MoveNorth()
		case South:
			santa.MoveSouth()
		case East:
			santa.MoveEast()
		case West:
			santa.MoveWest()
		}
		grid.Set(santa.Position, true)
	}

	return grid.Len()
}

func part2(moves []Move) int {
	grid := NewInfiniteGrid[bool]()
	santas := []*Santa{NewSanta(), NewSanta()}

	for i, move := range moves {
		switch move {
		case North:
			santas[i%2].MoveNorth()
		case South:
			santas[i%2].MoveSouth()
		case East:
			santas[i%2].MoveEast()
		case West:
			santas[i%2].MoveWest()
		}
		grid.Set(santas[i%2].Position, true)
	}

	return grid.Len()
}

func main() {
	moves, err := readInput()
	if err != nil {
		panic(err)
	}

	println("Part 1:", part1(moves))
	println("Part 2:", part2(moves))
}
