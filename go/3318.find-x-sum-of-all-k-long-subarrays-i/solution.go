// Created by none at 2025/11/04 12:07
// leetgo: dev
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type Pair struct {
	freq int
	x    int
}

type Heap []Pair

func (h Heap) Len() int {
	return len(h)
}

func (h *Heap) Push(item any) {
	(*h) = append((*h), item.(Pair))
}

func (h Heap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h Heap) Less(i, j int) bool {
	return h[i].freq < h[j].freq || h[i].freq == h[j].freq && h[i].x < h[j].x
}

func (h *Heap) Pop() any {
	item := (*h)[h.Len()-1]
	*h = (*h)[:h.Len()-1]
	return item
}

func findXSum(nums []int, k int, x int) []int {
	cnt := make(map[int]int)
	for i := range k - 1 {
		cnt[nums[i]]++
	}
	var res []int
	for i := k - 1; i < len(nums); i++ {
		cnt[nums[i]]++
		var q []Pair
		for k, f := range cnt {
			q = append(q, Pair{f, k})
		}
		sort.Slice(q, func(i2, j int) bool {
			return q[i2].freq > q[j].freq || q[i2].freq == q[j].freq && q[i2].x > q[j].x
		})
		// fmt.Println(cnt, q)
		s := 0
		for j := range min(x, len(q)) {
			s += q[j].freq * q[j].x
		}

		res = append(res, s)
		cnt[nums[i-(k-1)]]--
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	x := Deserialize[int](ReadLine(stdin))
	ans := findXSum(nums, k, x)

	fmt.Println("\noutput:", Serialize(ans))
}
