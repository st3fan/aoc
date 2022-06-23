package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"time"
)

type Grid[T comparable] struct {
	data [][]T
}

func LoadGrid[T comparable](path string, convert func(c byte) (T, error)) (*Grid[T], error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}

	defer file.Close()

	var data [][]T

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		row := make([]T, len(line))
		for x := 0; x < len(line); x++ {
			e, err := convert(line[x])
			if err != nil {
				return nil, err
			}
			row[x] = e
		}
		data = append(data, row)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return &Grid[T]{data: data}, nil
}

func NewGrid[T comparable](width int, height int, e T) *Grid[T] {
	var data [][]T
	for y := 0; y < height; y++ {
		row := make([]T, width)
		for x := 0; x < width; x++ {
			row[x] = e
		}
		data = append(data, row)
	}
	return &Grid[T]{data: data}
}

func (g *Grid[T]) Copy() *Grid[T] {
	var data [][]T
	for y := 0; y < g.Height(); y++ {
		row := make([]T, g.Width())
		copy(row, g.data[y])
		data = append(data, row)
	}
	return &Grid[T]{data: data}
}

func (g *Grid[T]) Width() int {
	return len(g.data[0])
}

func (g *Grid[T]) Height() int {
	return len(g.data)
}

func (g *Grid[T]) Get(x int, y int) T {
	return g.data[y][x]
}

func (g *Grid[T]) Set(x int, y int, e T) {
	g.data[y][x] = e
}

//

const (
	Empty = 0
	East  = 1
	South = 2
)

func convertGridElement(c byte) (int, error) {
	switch c {
	case '.':
		return Empty, nil
	case '>':
		return East, nil
	case 'v':
		return South, nil
	}
	return -1, errors.New("Unexpected grid value")
}

func step(grid *Grid[int]) (*Grid[int], int) {
	moved := 0

	src := grid
	dst := src.Copy()

	for y := 0; y < src.Height(); y++ {
		for x := 0; x < src.Width(); x++ {
			if src.Get(x, y) == East && src.Get((x+1)%src.Width(), y) == Empty {
				dst.Set((x+1)%src.Width(), y, East)
				dst.Set(x, y, Empty)
				moved++
			}
		}
	}

	src = dst
	dst = src.Copy()

	for y := 0; y < src.Height(); y++ {
		for x := 0; x < src.Width(); x++ {
			if src.Get(x, y) == South && src.Get(x, (y+1)%src.Height()) == Empty {
				dst.Set(x, (y+1)%src.Height(), South)
				dst.Set(x, y, Empty)
				moved++
			}
		}
	}

	return dst, moved
}

func part1() int {
	grid, err := LoadGrid("day25.input", convertGridElement)
	if err != nil {
		log.Fatal("Could not load input:", err)
	}

	steps := 1
	for {
		updatedGrid, moved := step(grid)
		if moved == 0 {
			break
		}

		steps += 1
		grid = updatedGrid
	}

	return steps
}

func main() {
	start := time.Now()
	fmt.Printf("Part one: %d (%v)", part1(), time.Now().Sub(start))
}
