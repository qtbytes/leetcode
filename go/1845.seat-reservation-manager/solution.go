// Created by none at 2024/09/30 13:47
// leetgo: 1.4.9
// https://leetcode.cn/problems/seat-reservation-manager/

package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

type SeatManager []int

func (h SeatManager) Len() int           { return len(h) }
func (h SeatManager) Less(i, j int) bool { return h[i] < h[j] }
func (h SeatManager) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *SeatManager) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *SeatManager) Pop() any {
	n := len(*h)
	x := (*h)[n-1]
	*h = (*h)[0 : n-1]
	return x
}

func Constructor(n int) SeatManager {
	h := make([]int, n)
	for i := 0; i < n; i++ {
		h[i] = i + 1
	}
	return h
}

func (s *SeatManager) Reserve() int {
	return heap.Pop(s).(int)
}

func (s *SeatManager) Unreserve(seatNumber int) {
	heap.Push(s, seatNumber)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	ops := Deserialize[[]string](ReadLine(stdin))
	params := MustSplitArray(ReadLine(stdin))
	output := make([]string, 0, len(ops))
	output = append(output, "null")

	constructorParams := MustSplitArray(params[0])
	n := Deserialize[int](constructorParams[0])
	obj := Constructor(n)

	for i := 1; i < len(ops); i++ {
		switch ops[i] {
		case "reserve":
			ans := Serialize(obj.Reserve())
			output = append(output, ans)
		case "unreserve":
			methodParams := MustSplitArray(params[i])
			seatNumber := Deserialize[int](methodParams[0])
			obj.Unreserve(seatNumber)
			output = append(output, "null")
		}
	}
	fmt.Println("\noutput:", JoinArray(output))
}
