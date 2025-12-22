// Created by none at 2025/12/22 21:14
// leetgo: dev
// https://leetcode.com/problems/maximum-score-after-binary-swaps/
// https://leetcode.com/contest/biweekly-contest-172/problems/maximum-score-after-binary-swaps/

package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"

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

func maximumScore(nums []int, s string) int64 {
	n := len(nums)
	i, j := 0, n-1
	ans := 0
	for ; i <= j && s[i] == '1'; i++ {
		ans += nums[i]
	}
	for ; i <= j && s[j] == '0'; j-- {
	}

	h := &IntHeap{}
	size := 0

	for k := j; k >= i; k-- {
		heap.Push(h, nums[k])
		if s[k] == '1' {
			size++
		}
		for h.Len() > size {
			heap.Pop(h)
		}
	}
	for _, x := range *h {
		ans += x
	}

	return int64(ans)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	s := Deserialize[string](ReadLine(stdin))
	ans := maximumScore(nums, s)

	fmt.Println("\noutput:", Serialize(ans))
}
