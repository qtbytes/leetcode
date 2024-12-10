// Created by none at 2024/12/09 13:56
// leetgo: 1.4.9
// https://leetcode.com/problems/special-array-ii/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func isArraySpecial(nums []int, queries [][]int) []bool {
	n := len(nums)
	f := make([]int, n)
	for i := 1; i < n; i++ {
		if nums[i]&1 != nums[i-1]&1 {
			f[i] = f[i-1]
		} else {
			f[i] = i
		}
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		if q[0] >= f[q[1]] {
			ans[i] = true
		}
	}
	return ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	queries := Deserialize[[][]int](ReadLine(stdin))
	ans := isArraySpecial(nums, queries)

	fmt.Println("\noutput:", Serialize(ans))
}
