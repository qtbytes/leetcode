// Created by none at 2024/11/13 13:39
// leetgo: 1.4.9
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func countFairPairs(nums []int, lower int, upper int) int64 {
	sort.Ints(nums)
	res := 0
	for i, x := range nums {
		l := sort.Search(i, func(i int) bool {
			return x+nums[i] >= lower
		})
		r := sort.Search(i, func(i int) bool {
			return x+nums[i] > upper
		})
		res += r - l
		// fmt.Println(l, r, nums[l], nums[r])
	}
	return int64(res)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	lower := Deserialize[int](ReadLine(stdin))
	upper := Deserialize[int](ReadLine(stdin))
	ans := countFairPairs(nums, lower, upper)

	fmt.Println("\noutput:", Serialize(ans))
}
