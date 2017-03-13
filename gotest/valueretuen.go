package main

import(
	"fmt"
)


func split( num int) (x, y int) {
	x = num * 12 / 10
	y = x - num
	return
}

func main() {
	fmt.Println(split(10))
}
