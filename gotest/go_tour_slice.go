package main

import (
	"golang.org/x/tour/pic"
	"math"
)

//实现 Pic 。它应当返回一个长度为 dy 的切片，其中每个元素是一个长度为 dx ，元素类型为 uint8 的切片

func Pic(dx, dy int) [][]uint8 {
	myret := make([][]uint8, dy)
	for i := 0; i < dy ; i++{
		myret[i] = make([]uint8, dx)
		for j := 0; j < dx ; j++ {
			myret[i][j] = uint8(float64(j) * math.Log(float64(i)))
		}

	}
	return myret
}


func main() {
	pic.Show(Pic)
}
