// Created by none at 2025/09/25 10:05
// leetgo: dev
// https://leetcode.com/problems/triangle/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func minimumTotal(triangle [][]int) int {
	prev := make([]int, 1)
	for _, row := range triangle {
		dp := make([]int, len(row))
		for j, x := range row {
			if j == 0 {
				dp[j] = prev[j] + x
			} else if j < len(prev) {
				dp[j] = min(prev[j], prev[j-1]) + x
			} else {
				dp[j] = prev[j-1] + x
			}
		}
		prev = dp
	}
	return slices.Min(prev)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	triangle := Deserialize[[][]int](ReadLine(stdin))
	ans := minimumTotal(triangle)

	fmt.Println("\noutput:", Serialize(ans))
}
