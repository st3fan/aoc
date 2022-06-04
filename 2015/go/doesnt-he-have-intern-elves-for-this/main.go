package main

import (
	"io/ioutil"
	"regexp"
	"strings"
)

func CountIf[T any](values []T, f func(value T) bool) int {
	total := 0
	for i := range values {
		if f(values[i]) {
			total += 1
		}
	}
	return total
}

// This is way more complicated than it should have to be because
// Go doesn't have the greatest regular expression engine.

func containsTwice(s string) bool {
	for i := 'a'; i <= 'z'; i++ {
		if strings.Contains(s, string(i)+string(i)) {
			return true
		}
	}
	return false
}

func hasRepeatingLetterWithOneInBetween(secret string) bool {
	for i := 0; i < len(secret)-2; i++ {
		if secret[i] == secret[i+2] {
			return true
		}
	}
	return false
}

func hasPairOfTwoLetters(secret string) bool {
	for i := 0; i < len(secret)-1; i++ {
		if strings.Contains(secret[i+2:], secret[i:i+2]) {
			return true
		}
	}
	return false
}

func isNice1(s string) bool {
	if len(regexp.MustCompile(`[aeuio]`).FindAllString(s, -1)) < 3 {
		return false
	}
	if !containsTwice(s) {
		return false
	}
	if regexp.MustCompile(`(ab|cd|pq|xy)`).MatchString(s) {
		return false
	}
	return true
}

func isNice2(password string) bool {
	if !hasRepeatingLetterWithOneInBetween(password) {
		return false
	}
	if !hasPairOfTwoLetters(password) {
		return false
	}
	return true
}

func part1(input []string) int {
	return CountIf(input, isNice1)
}

func part2(input []string) int {
	return CountIf(input, isNice2)
}

func readInput() ([]string, error) {
	bytes, err := ioutil.ReadFile("input.txt")
	if err != nil {
		return nil, err
	}
	return strings.Split(string(bytes), "\n"), nil
}

func main() {
	input, err := readInput()
	if err != nil {
		panic(err)
	}
	println("Part 1:", part1(input))
	println("Part 2:", part2(input))
}
