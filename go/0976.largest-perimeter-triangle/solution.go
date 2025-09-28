// Created by none at 2025/09/28 11:05
// leetgo: dev
// https://leetcode.com/problems/largest-perimeter-triangle/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func largestPerimeter(nums []int) int {
	sort.Ints(nums)

	for i := len(nums) - 1; i >= 2; i-- {
		if nums[i] < nums[i-1]+nums[i-2] {
			return nums[i] + nums[i-1] + nums[i-2]
		}
	}

	return 0
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := largestPerimeter(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
