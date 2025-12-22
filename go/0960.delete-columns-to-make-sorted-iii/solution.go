// Created by none at 2025/12/22 13:54
// leetgo: dev
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func minDeletionSize(strs []string) int {
	m := len(strs)
	n := len(strs[0])

	dp := make([]int, n)

	for j := n - 1; j >= 0; j-- {
		dp[j] = 1
		for k := j + 1; k < n; k++ {
			ok := true
			for i := range m {
				if strs[i][k] < strs[i][j] {
					ok = false
				}
			}
			if ok {
				dp[j] = max(dp[j], 1+dp[k])
			}
		}
	}

	ans := n - slices.Max(dp)
	return ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	strs := Deserialize[[]string](ReadLine(stdin))
	ans := minDeletionSize(strs)

	fmt.Println("\noutput:", Serialize(ans))
}
