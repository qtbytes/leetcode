// Created by none at 2024/10/07 09:25
// leetgo: 1.4.9
// https://leetcode.cn/problems/minimum-number-of-refueling-stops/

package main

import (
	"bufio"
	"fmt"
	"os"

	"container/heap"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func minRefuelStops(target int, startFuel int, stations [][]int) int {
	stations = append(stations, []int{target, 0})
	q := &IntHeap{}
	fuel := startFuel
	res := 0
	y := 0
	for _, s := range stations {
		x, f := s[0], s[1]
		d := x - y
		y = x
		for fuel < d && q.Len() > 0 {
			res += 1
			fuel += heap.Pop(q).(int)
		}
		if fuel < d {
			return -1
		}
		fuel -= d
		heap.Push(q, f)
	}

	return res

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	target := Deserialize[int](ReadLine(stdin))
	startFuel := Deserialize[int](ReadLine(stdin))
	stations := Deserialize[[][]int](ReadLine(stdin))
	ans := minRefuelStops(target, startFuel, stations)

	fmt.Println("\noutput:", Serialize(ans))
}
