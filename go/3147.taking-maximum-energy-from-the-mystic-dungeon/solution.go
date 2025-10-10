// Created by none at 2025/10/10 16:00
// leetgo: dev
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

const inf int = -1e6

func maximumEnergy(energy []int, k int) int {
	n := len(energy)
	dp := func(i int) int {
		res := inf
		for j := i; j < n; j += k {
			res = max(res, 0) + energy[j]
		}
		return res
	}
	res := inf
	for i := range k {
		res = max(res, dp(i))
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	energy := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := maximumEnergy(energy, k)

	fmt.Println("\noutput:", Serialize(ans))
}
