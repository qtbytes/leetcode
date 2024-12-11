// Created by none at 2024/12/11 10:10
// leetgo: 1.4.9
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maximumBeauty(nums []int, k int) int {
	sort.Ints(nums)
	l := 0
	n := len(nums)
	res := 0
	for r := 0; r < n; r++ {
		for l < r && nums[l]+2*k < nums[r] {
			l++
		}
		res = max(res, r-l+1)
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := maximumBeauty(nums, k)

	fmt.Println("\noutput:", Serialize(ans))
}
