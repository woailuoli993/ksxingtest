package main

import (
	"fmt"
	"math"
)

func add(x, y int) int {
	return x + y
}

func main() {
	// 包导出名应该为大写 即 首字母大写为 public  小写为 private
	fmt.Println(math.Pi)
	fmt.Print(
		add(24, 12))
}