package main

import (
	"fmt"
	"time"
)

func mydefer() {
	defer fmt.Println("my defer is done")  // defer 为栈模式

	fmt. Println(" diuleiloumou")

	defer fmt.Println(" done 2")

	fmt.Println("duilei2")
	defer  fmt.Println("done 3")
}

func main() {
	nowtime := time.Now().Weekday()
	fmt.Println(nowtime)
	switch time.Sunday {

	case nowtime + 1:
		fmt.Println("tomorrow!")
	case nowtime:
		fmt.Println("today")
		fallthrough
	default:
		fmt.Println("far away")

	}

	mydefer()
}
