// Created by none at 2025/12/07 10:30
// leetgo: dev
// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func countOdds(low int, high int) int {
	n := high - low + 1
	if n&1 == 0 {
		return n / 2
	}
	return n/2 + (low & 1)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	low := Deserialize[int](ReadLine(stdin))
	high := Deserialize[int](ReadLine(stdin))
	ans := countOdds(low, high)

	fmt.Println("\noutput:", Serialize(ans))
}
