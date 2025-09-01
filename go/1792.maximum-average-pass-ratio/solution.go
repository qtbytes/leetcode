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
	x     int
	y     int
}

type Heap struct {
	q []Item
}

func (h *Heap) Len() int {
	return len(h.q)
}

func (h *Heap) Less(i, j int) bool {
	return (*h).q[i].delta > (*h).q[j].delta
}

func (h *Heap) Push(item any) {
	(*h).q = append((*h).q, item.(Item))
}

func (h *Heap) Pop() any {
	item := (*h).q[h.Len()-1]
	(*h).q = (*h).q[:h.Len()-1]
	return item
}

func (h *Heap) Swap(i int, j int) {
	(*h).q[i], (*h).q[j] = (*h).q[j], (*h).q[i]
}

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
	h := &Heap{}
	heap.Init(h)
	for _, c := range classes {
		x, y := c[0], c[1]
		heap.Push(h, Item{float64(y-x) / float64(y+1) / float64(y), x, y})
	}

	for range extraStudents {
		item := heap.Pop(h).(Item)
		x, y := item.x+1, item.y+1
		heap.Push(h, Item{float64(y-x) / float64(y+1) / float64(y), x, y})
	}

	res := 0.0

	for _, item := range (*h).q {
		res += float64(item.x) / float64(item.y)
	}

	return res / float64(len(classes))
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	classes := Deserialize[[][]int](ReadLine(stdin))
	extraStudents := Deserialize[int](ReadLine(stdin))
	ans := maxAverageRatio(classes, extraStudents)

	fmt.Println("\noutput:", Serialize(ans))
}
