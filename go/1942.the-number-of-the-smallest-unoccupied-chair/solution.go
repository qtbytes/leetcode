// Created by none at 2024/10/11 12:48
// leetgo: 1.4.9
// https://leetcode.cn/problems/the-number-of-the-smallest-unoccupied-chair/

package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }

func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

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

type Pair struct {
	t      int
	arrive int // 1: arrive, -1:leave
	i      int // index
}

func smallestChair(times [][]int, targetFriend int) int {
	target := times[targetFriend][0]
	arrive := []Pair{}
	for i, time := range times {
		arrive = append(arrive, Pair{time[0], 1, i})
		arrive = append(arrive, Pair{time[1], -1, i})
	}
	sort.Slice(arrive, func(i, j int) bool {
		return arrive[i].t < arrive[j].t || arrive[i].t == arrive[j].t && arrive[i].arrive < arrive[j].arrive
	})
	chairs := &IntHeap{}
	for i := range len(times) {
		heap.Push(chairs, i)
	}

	record := make([]int, len(times))
	for _, p := range arrive {
		if p.t == target && p.arrive == 1 {
			return heap.Pop(chairs).(int)
		}
		if p.arrive == 1 {
			chair := heap.Pop(chairs).(int)
			record[p.i] = chair
		} else {
			chair := record[p.i]
			heap.Push(chairs, chair)
		}
	}

	return -1

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	times := Deserialize[[][]int](ReadLine(stdin))
	targetFriend := Deserialize[int](ReadLine(stdin))
	ans := smallestChair(times, targetFriend)

	fmt.Println("\noutput:", Serialize(ans))
}
