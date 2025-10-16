// Created by none at 2025/10/16 13:54
// leetgo: dev
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func findSmallestInteger(nums []int, value int) int {
	cnt := make([]int, value)
	for i := range nums {
		key := (nums[i]%value + value) % value
		cnt[key]++
	}

	key := 0

	for i, v := range cnt {
		if v < cnt[key] {
			key = i
		}
	}

	return key + cnt[key]*value
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	value := Deserialize[int](ReadLine(stdin))
	ans := findSmallestInteger(nums, value)

	fmt.Println("\noutput:", Serialize(ans))
}
