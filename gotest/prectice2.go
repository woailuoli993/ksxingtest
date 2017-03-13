package main

import "fmt"
//import "golang.org/x/tour/pic"

//实现 Pic 。它应当返回一个长度为 dy 的切片，其中每个元素是一个长度为 dx ，元素类型为 uint8 的切片

func Pic(dx, dy int) [][]uint8 {
	myret := make([][]uint8, dy)
	for i := 0; i < dy ; i++{
		for j := 0; j < dx ; j++ {
			myret := append(myret[i], uint8(dy*i+j))
		}

	}
	return myret
}

//func Pic(dx, dy int) [][]uint8 {
//	return [][]uint8{
//		[]uint8{uint8(dx), 2, 3},
//		[]uint8{uint8(dy), 2, 3},
//		[]uint8{3, 2, 3},
//		[]uint8{4, 2, 3},
//
//	}
//}

func main() {
	fmt.Println(Pic(10, 10))
	//pic.Show(Pic)
}
