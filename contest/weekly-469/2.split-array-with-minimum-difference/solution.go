// Created by none at 2025/09/28 15:24
// leetgo: dev
// https://leetcode.com/problems/split-array-with-minimum-difference/
// https://leetcode.com/contest/weekly-contest-469/problems/split-array-with-minimum-difference/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func splitArray(nums []int) int64 {
	n := len(nums)
	i := 0
	left := 0
	// 0..=i is incresing
	for i+1 < n && nums[i] < nums[i+1] {
		left += nums[i]
		i++
	}
	j := n - 1
	right := 0
	// j..=n-1 is decreasing
	for j > 0 && nums[j] < nums[j-1] {
		right += nums[j]
		j--
	}
	// fmt.Println(i, j, left, right)
	if i != j && i+1 != j {
		return -1
	}
	if i == j {
		return int64(min(abs(left+nums[i]-right), abs(left-nums[i]-right)))
	}
	return int64(abs(left - right))
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := splitArray(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
