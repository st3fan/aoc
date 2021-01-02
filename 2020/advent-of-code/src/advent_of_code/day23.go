package main

import (
	"container/ring"
	"os"
)

func findMin(cups map[int]*ring.Ring, removed *ring.Ring) *ring.Ring {
	for i := 1; i <= 4; i++ {
		if p := cups[i]; p != nil {
			if cups[i] != removed && cups[i] != removed.Next() && cups[i] != removed.Next().Next() {
				return p
			}
		}
	}
	return nil
}

func findMax(cups map[int]*ring.Ring, removed *ring.Ring) *ring.Ring {
	for i := 1_000_000; i >= 1_000_000-4; i-- {
		if p := cups[i]; p != nil {
			if cups[i] != removed && cups[i] != removed.Next() && cups[i] != removed.Next().Next() {
				return p
			}
		}
	}
	return nil
}

func part2() {

	// Setup the cups in a ring
	cups := ring.New(1_000_000)

	r := cups
	r.Value = 4

	r = r.Next()
	r.Value = 1

	r = r.Next()
	r.Value = 8

	r = r.Next()
	r.Value = 9

	r = r.Next()
	r.Value = 7

	r = r.Next()
	r.Value = 6

	r = r.Next()
	r.Value = 2

	r = r.Next()
	r.Value = 3

	r = r.Next()
	r.Value = 5

	for i := 10; i <= 1_000_000; i++ {
		r = r.Next()
		r.Value = i
	}

	// Also put all the cups in a map for easy checks (min, max, near O(1) lookup)

	cupsByNumber := map[int]*ring.Ring{}

	cupsByNumber[cups.Value.(int)] = cups
	for p := cups.Next(); p != cups; p = p.Next() {
		cupsByNumber[p.Value.(int)] = p
	}

	// Move the cups

	current := cups

	for n := 0; n < 10_000_000; n++ {
		// The crab picks up the three cups that are immediately
		// clockwise of the current cup.

		removed := current.Unlink(3)

		delete(cupsByNumber, removed.Value.(int))
		delete(cupsByNumber, removed.Next().Value.(int))
		delete(cupsByNumber, removed.Next().Next().Value.(int))

		// The crab selects a destination cup: the cup with a label
		// equal to the current cup's label minus one. If this would
		// select one of the cups that was just picked up, the crab
		// will keep subtracting one until it finds a cup that wasn't
		// just picked up. If at any point in this process the value
		// goes below the lowest value on any cup's label, it wraps
		// around to the highest value on any cup's label instead.

		var dst *ring.Ring

		min := findMin(cupsByNumber, removed)

		v := current.Value.(int) -1

		for {
			if v < min.Value.(int) {
				break
			}

			if p := cupsByNumber[v]; p != nil {
				dst = p
				break
			}

			v = v - 1
		}

		if dst == nil {
			dst = findMax(cupsByNumber, removed)
		}

		// The crab places the cups it just picked up so that they are
		// immediately clockwise of the destination cup.

		dst.Link(removed)

		cupsByNumber[removed.Value.(int)] = removed
		cupsByNumber[removed.Next().Value.(int)] = removed.Next()
		cupsByNumber[removed.Next().Next().Value.(int)] = removed.Next().Next()

		// The crab selects a new current cup: the cup which is
		// immediately clockwise of the current cup.

		current = current.Next()
	}

	// And we're done

	a := cupsByNumber[1].Next().Value.(int)
	println("a = ", a)

	b := cupsByNumber[1].Next().Next().Value.(int)
	println("b = ", b)

	println("answer = ", a*b)
}

func main() {
	part2()
}
