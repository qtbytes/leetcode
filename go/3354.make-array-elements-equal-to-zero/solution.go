// Created by none at 2025/10/28 21:31
// leetgo: dev
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func countValidSelections(nums []int) int {
	right := 0
	for _, x := range nums {
		right += x
	}
	left := 0
	res := 0
	for _, x := range nums {
		left += x
		right -= x
		if x == 0 {
			// try left
			if left == right || left == right+1 {
				res++
			}
			// try right
			if left == right || left == right-1 {
				res++
			}
		}
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := countValidSelections(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
