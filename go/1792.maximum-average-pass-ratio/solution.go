// Created by none at 2025/09/01 12:18
// leetgo: dev
// https://leetcode.com/problems/maximum-average-pass-ratio/

package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type Item struct {
	delta float64
	x, y  int
}

type Heap []Item

func (h Heap) Len() int {
	return len(h)
}

func (h Heap) Less(i, j int) bool {
	return h[i].delta > h[j].delta
}

func (h *Heap) Push(item any) {
	*h = append((*h), item.(Item))
}

func (h *Heap) Pop() any {
	item := (*h)[h.Len()-1]
	*h = (*h)[:h.Len()-1]
	return item
}

func (h *Heap) Swap(i int, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
	n := len(classes)

	h := make(Heap, n)
	for i, c := range classes {
		x, y := c[0], c[1]
		h[i] = Item{float64(y-x) / float64(y+1) / float64(y), x, y}
	}
	heap.Init(&h)

	for range extraStudents {
		h[0].x++
		h[0].y++
		x, y := h[0].x, h[0].y
		h[0].delta = float64(y-x) / float64(y+1) / float64(y)
		heap.Fix(&h, 0)
	}

	res := 0.0
	for _, item := range h {
		res += float64(item.x) / float64(item.y)
	}
	return res / float64(n)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	classes := Deserialize[[][]int](ReadLine(stdin))
	extraStudents := Deserialize[int](ReadLine(stdin))
	ans := maxAverageRatio(classes, extraStudents)

	fmt.Println("\noutput:", Serialize(ans))
}
