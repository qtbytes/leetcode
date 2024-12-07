// Created by none at 2024/12/07 15:31
// leetgo: 1.4.9
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func minimumSize(nums []int, maxOperations int) int {
	l, r := 1, slices.Max(nums)
	for l < r {
		mid := (l + r) >> 1
		cnt := 0
		for _, x := range nums {
			if x > mid {
				cnt += (x - 1) / mid
				if cnt > maxOperations {
					break
				}
			}
		}
		if cnt <= maxOperations {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return l
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	maxOperations := Deserialize[int](ReadLine(stdin))
	ans := minimumSize(nums, maxOperations)

	fmt.Println("\noutput:", Serialize(ans))
}
