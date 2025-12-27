// Created by none at 2025/12/27 12:22
// leetgo: dev
// https://leetcode.com/problems/meeting-rooms-iii/

package main

import (
	"bufio"
	"cmp"
	"fmt"
	"os"
	"slices"

	"github.com/emirpasic/gods/v2/queues/priorityqueue"
	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

type Pair struct{ end, index int }

func pairComparator(a, b Pair) int {
	if a.end != b.end {
		return cmp.Compare(a.end, b.end) // smaller end comes first
	}
	return cmp.Compare(a.index, b.index) // tie-break by smaller index
}
func mostBooked(n int, meetings [][]int) int {
	slices.SortFunc(meetings, func(a, b []int) int { return a[0] - b[0] })

	unused := priorityqueue.New[int]()
	for i := range n {
		unused.Enqueue(i)
	}
	// fmt.Println(meetings)
	using := priorityqueue.NewWith(pairComparator)
	cnt := make([]int, n)
	for _, m := range meetings {
		start, end := m[0], m[1]
		for !using.Empty() {
			p, _ := using.Peek()
			if p.end <= start {
				using.Dequeue()
				unused.Enqueue(p.index)
			} else {
				break
			}
		}
		if !unused.Empty() {
			i, _ := unused.Dequeue()
			cnt[i]++
			using.Enqueue(Pair{end, i})
		} else {
			p, _ := using.Dequeue()
			cnt[p.index]++
			using.Enqueue(Pair{p.end + (end - start), p.index})
		}
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
