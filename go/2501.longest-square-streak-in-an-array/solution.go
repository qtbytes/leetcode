// Created by none at 2024/10/28 11:56
// leetgo: 1.4.9
// https://leetcode.com/problems/longest-square-streak-in-an-array/

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func longestSquareStreak(nums []int) int {
	sort.Slice(nums, func(i, j int) bool { return nums[i] < nums[j] })
	f := make(map[int]int)
	res := 0

	for _, x := range nums {
		f[x] = 1
		y := int(math.Sqrt(float64(x)))
		if y*y == x {
			f[x] += f[y]
		} 
		res = max(res, f[x])
	}

	if res == 1 {
		return -1
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := longestSquareStreak(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
