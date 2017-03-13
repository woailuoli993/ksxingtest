package main

import (
	"fmt"
)

type mysu struct {
	he int
	yu int
}

func main() {
	fmt.Println(mysu{1, 3})
	nsu := mysu{2, 4}
	fmt.Println(nsu.he)
	myyu := &nsu
	fmt.Println(myyu.yu)
	fmt.Println(*myyu)

	nsu2 := mysu{yu : 23}
	fmt.Println(nsu2)
}

