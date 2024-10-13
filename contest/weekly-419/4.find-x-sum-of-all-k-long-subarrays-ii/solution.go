// Created by none at 2024/10/13 15:11
// leetgo: 1.4.9
// https://leetcode.cn/problems/find-x-sum-of-all-k-long-subarrays-ii/
// https://leetcode.cn/contest/weekly-contest-419/problems/find-x-sum-of-all-k-long-subarrays-ii/

package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type Pair struct {
	f, x int
}

type MaxHeap []Pair

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i].f > h[j].f || h[i].f == h[j].f && h[i].x > h[j].x }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(Pair))
}
func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type MinHeap []Pair

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i].f < h[j].f || h[i].f == h[j].f && h[i].x < h[j].x }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(Pair))
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func findXSum(nums []int, k int, cap int) []int64 {
	n := len(nums)
	freq := make(map[int]int)
	mx := &MaxHeap{}
	mn := &MinHeap{}
	for i := range k {
		x := nums[i]
		freq[x]++
		heap.Push(mn, Pair{freq[x], x})
		if mn.Len() > cap {
			item := heap.Pop(mn).(Pair)
			if item.f == freq[item.x] {
				heap.Push(mx, item)
			}
		}
	}
	s := 0
	for i := range mn.Len() {
		s += (*mn)[i].x * (*mn)[i].f

	}
	res := []int64{}
	for i := k; i < n; i++ {
		fmt.Println(s, mn, mx, freq)
		res = append(res, int64(s))
		x := nums[i]
		y := nums[i-k]
		freq[x]++
		for mx.Len() > 0 && freq[(*mx)[0].x] != (*mx)[0].f {
			heap.Pop(mx)
		}
		heap.Push(mx, Pair{freq[x], x})
		if (*mn)[0].f < (*mx)[0].f || (*mn)[0].f == (*mx)[0].f && (*mn)[0].x < (*mx)[0].x {
			s += x
			item := heap.Pop(mx).(Pair)
			heap.Push(mn, item)
			item = heap.Pop(mn).(Pair)
			if item.f == freq[item.x] {
				heap.Push(mx, item)
				s -= item.x
			}
		}
		freq[y]--
	}
	res = append(res, int64(s))
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
