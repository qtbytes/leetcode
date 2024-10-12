// Created by none at 2024/10/12 11:28
// leetgo: 1.4.9
// https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/

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
func minGroups(intervals [][]int) int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	groups := &IntHeap{}

	for _, interval := range intervals {
		x, y := interval[0], interval[1]
		if groups.Len() > 0 && (*groups)[0] < x {
			heap.Pop(groups)
		}
		heap.Push(groups, y)
	}

	return groups.Len()

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	intervals := Deserialize[[][]int](ReadLine(stdin))
	ans := minGroups(intervals)

	fmt.Println("\noutput:", Serialize(ans))
}
