package main

import (
	"log"
	"math"
	"os"
	"runtime"
	"strconv"
	"strings"
	"sync"
	"time"
)

func MustAtoi(s string) int {
	n, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return n
}

//

type Mapping struct {
	Dst int
	Src int
	Len int
}

func NewMappingFromString(s string) Mapping {
	c := strings.Fields(strings.TrimSpace(s))
	return Mapping{
		Dst: MustAtoi(c[0]),
		Src: MustAtoi(c[1]),
		Len: MustAtoi(c[2]),
	}
}

func (m Mapping) MapLocation(location int) (int, bool) {
	if location >= m.Src && location <= (m.Src+m.Len) {
		return m.Dst + (location - m.Src), true
	}
	return 0, false
}

//

func parseSeedNumbers(s string) []int {
	var numbers []int
	for _, s := range strings.Fields(s)[1:] {
		numbers = append(numbers, MustAtoi(s))
	}
	return numbers
}

func parseMappings(sections []string) [][]Mapping {
	var result [][]Mapping
	for _, section := range sections {
		var mappings []Mapping
		for _, s := range strings.Split(strings.TrimSpace(section), "\n")[1:] {
			mapping := NewMappingFromString(s)
			mappings = append(mappings, mapping)
		}
		result = append(result, mappings)
	}
	return result
}

func readInput() ([]int, [][]Mapping) {
	contents, _ := os.ReadFile("input.txt")
	sections := strings.Split(string(contents), "\n\n")

	mappings := parseMappings(sections[1:])
	seedNumbers := parseSeedNumbers(sections[0])

	return seedNumbers, mappings
}

//

func findLocation(mappings []Mapping, location int) int {
	for _, mapping := range mappings {
		if n, ok := mapping.MapLocation(location); ok {
			return n
		}
	}
	return location
}

func findFinalLocation(allMappings [][]Mapping, location int) int {
	for _, mappings := range allMappings {
		location = findLocation(mappings, location)
	}
	return location
}

//

func part1() int {
	seedNumbers, mappings := readInput()

	min := math.MaxInt
	for _, seedNumber := range seedNumbers {
		n := findFinalLocation(mappings, seedNumber)
		if n < min {
			min = n
		}
	}

	return min
}

type Job struct {
	Start     int
	End       int
	JobIndex  int
	TotalJobs int
}

func (job Job) Run(mappings [][]Mapping) int {
	min := math.MaxInt
	for i := job.Start; i <= job.End; i++ {
		if n := findFinalLocation(mappings, i); n < min {
			min = n
		}
	}
	return min
}

type Result struct {
	Min      int
	JobIndex int
}

const JobSize = 5_000_000

func part2() int {
	seedNumbers, mappings := readInput()

	var jobs []Job
	jobIndex := 0

	for i := 0; i < len(seedNumbers)/2; i++ {
		start := seedNumbers[i*2]
		end := start + seedNumbers[i*2+1]

		// log.Printf("Job: %d - %d\n", start, end)

		for n := start; n <= end; n += JobSize {
			jobs = append(jobs, Job{Start: n, End: min(end, n+JobSize), JobIndex: jobIndex})
			jobIndex += 1
		}
	}

	for i := range jobs {
		jobs[i].TotalJobs = len(jobs)
	}

	//

	// for _, job := range jobs {
	// 	log.Printf("%v\n", job)
	// }

	// Run the work

	// min := math.MaxInt
	// for _, job := range jobs {
	// 	log.Printf("Running job <%+v>\n", job)
	// 	if n := job.Run(mappings); n < min {
	// 		min = n
	// 	}
	// }

	queue := make(chan Job, len(jobs))
	var wg sync.WaitGroup

	for _, job := range jobs {
		queue <- job
	}

	close(queue)

	globalMin := math.MaxInt
	var globalLock sync.Mutex

	wg.Add(runtime.NumCPU())

	for i := 0; i < runtime.NumCPU(); i++ {
		go func() {
			min := math.MaxInt
			for {
				job, ok := <-queue
				if !ok {
					break
				}
				if n := job.Run(mappings); n < min {
					min = n
				}
			}

			globalLock.Lock()
			defer globalLock.Unlock()

			if min < globalMin {
				globalMin = min
			}

			wg.Done()
		}()
	}

	wg.Wait()

	return globalMin
}

func main() {
	if true {
		t := time.Now()
		n := part1()
		log.Printf("Part 1: %d (%s)\n", n, time.Since(t))
	}

	if true {
		t := time.Now()
		n := part2()
		log.Printf("Part 2: %d (%s)\n", n, time.Since(t))
	}
}
