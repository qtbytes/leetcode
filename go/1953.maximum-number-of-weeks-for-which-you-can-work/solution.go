// Created by none at 2024/10/21 19:35
// leetgo: 1.4.9
// https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func numberOfWeeks(milestones []int) int64 {
	max := slices.Max(milestones)
	sum := 0
	for _, x := range milestones {
		sum += x
	}
	if max*2 <= sum {
		return int64(sum)
	}
	return int64(2*(sum-max) + 1)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	milestones := Deserialize[[]int](ReadLine(stdin))
	ans := numberOfWeeks(milestones)

	fmt.Println("\noutput:", Serialize(ans))
}
