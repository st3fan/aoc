package main

import (
	"crypto/md5"
	"fmt"
	"math"
)

const Input = "bgvyzdsv"

func part1(input string) int {
	for i := 1; i < math.MaxInt; i++ {
		hash := md5.Sum([]byte(fmt.Sprintf("%s%d", input, i)))
		if hash[0] == 0 && hash[1] == 0 && hash[2]&0xf0 == 0 {
			return i
		}
	}
	return 0
}

func part2(input string) int {
	for i := 1; i < math.MaxInt; i++ {
		hash := md5.Sum([]byte(fmt.Sprintf("%s%d", input, i)))
		if hash[0] == 0 && hash[1] == 0 && hash[2] == 0 {
			return i
		}
	}
	return 0
}

func main() {
	println("Part 1:", part1(Input))
	println("Part 2:", part2(Input))
}
