// Created by none at 2025/12/27 12:22
// leetgo: dev
// https://leetcode.com/problems/meeting-rooms-iii/

package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type Pair struct{ end, index int }
type ItemHeap []Pair

func (h ItemHeap) Len() int { return len(h) }
func (h ItemHeap) Less(i, j int) bool {
	return h[i].end < h[j].end || h[i].end == h[j].end && h[i].index < h[j].index
}
func (h ItemHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *ItemHeap) Push(x any) {
	*h = append(*h, x.(Pair))
}

func (h *ItemHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func mostBooked(n int, meetings [][]int) int {
	slices.SortFunc(meetings, func(a, b []int) int { return a[0] - b[0] })
	unused := &IntHeap{}
	for i := range n {
		heap.Push(unused, i)
	}
	// fmt.Println(meetings)
	using := &ItemHeap{}
	cnt := make([]int, n)
	for _, m := range meetings {
		start, end := m[0], m[1]
		for using.Len() > 0 && (*using)[0].end <= start {
			heap.Push(unused, heap.Pop(using).(Pair).index)
		}
		if len(*unused) > 0 {
			i := (heap.Pop(unused)).(int)
			cnt[i]++
			heap.Push(using, Pair{end, i})
		} else {
			p := heap.Pop(using).(Pair)
			cnt[p.index]++
			heap.Push(using, Pair{p.end + (end - start), p.index})
		}
		// fmt.Println(unused, using)
	}

	ans := 0
	for i, x := range cnt {
		if x > cnt[ans] {
			ans = i
		}
	}
	return ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	meetings := Deserialize[[][]int](ReadLine(stdin))
	ans := mostBooked(n, meetings)

	fmt.Println("\noutput:", Serialize(ans))
}
