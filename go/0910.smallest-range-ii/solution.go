// Created by none at 2024/10/20 10:04
// leetgo: 1.4.9
// https://leetcode.cn/problems/smallest-range-ii/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
func smallestRangeII(nums []int, k int) int {
	sort.Slice(nums, func(i, j int) bool { return nums[i] < nums[j] })
	n := len(nums)

	last := nums[n-1]
	res := last - nums[0]
	// nums[..i] all increase
	// nums[i..] all decrease

	for i := range n - 1 {
		x := nums[i]
		cur := abs(max(x+k, last-k) - min(nums[0]+k, nums[i+1]-k))
		res = min(res, cur)
	}
	return res

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := smallestRangeII(nums, k)

	fmt.Println("\noutput:", Serialize(ans))
}
