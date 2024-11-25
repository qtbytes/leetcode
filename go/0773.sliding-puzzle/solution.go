// Created by none at 2024/11/25 14:47
// leetgo: 1.4.9
// https://leetcode.com/problems/sliding-puzzle/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
func encode(nums []int) int {
	res := 0
	for i, x := range nums {
		res |= x << (3 * i)
	}
	return res
}

func slidingPuzzle(board [][]int) int {
	next := [][]int{{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}}
	visit := make(map[int]bool)
	target := encode([]int{1, 2, 3, 4, 5, 0})
	nums := []int{}
	for _, row := range board {
		nums = append(nums, row...)
	}
	s := encode(nums)
	if s == target {
		return 0
	}
	visit[s] = true
	q := [][]int{nums}
	t := 0
	for len(q) > 0 {
		fmt.Println(q)
		q_next := [][]int{}
		for _, nums := range q {
			x := 0 // zero
			for i, y := range nums {
				if y == 0 {
					x = i
					break
				}
			}
			// swap 0 and neighbor
			for _, y := range next[x] {
				nums[x], nums[y] = nums[y], nums[x]
				s := encode(nums)
				if s == target {
					return t + 1
				}
				if _, ok := visit[s]; !ok {
					q_next = append(q_next, append([]int(nil), nums...))
					visit[s] = true
				}
				nums[x], nums[y] = nums[y], nums[x]
			}
		}
		q = q_next
		t++
	}

	return -1

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	board := Deserialize[[][]int](ReadLine(stdin))
	ans := slidingPuzzle(board)

	fmt.Println("\noutput:", Serialize(ans))
}
