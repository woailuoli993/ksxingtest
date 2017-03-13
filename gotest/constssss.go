package main

import (
	"fmt"
)

const (
	Pi = 3.14
	duibu bool = true
	big = 1 << 100
)

func forfunc() int {
	sum := 0
	for i := 1; i < 10; i++ {
		sum += i
	}
	return sum
}

func whilefunc () {
	sum := 0
	for sum < 100 {
		sum += 1
		fmt.Println(sum)

	}
}
func main() {
	ret := forfunc()
	fmt.Println(ret)
	whilefunc()
	for {}
}

