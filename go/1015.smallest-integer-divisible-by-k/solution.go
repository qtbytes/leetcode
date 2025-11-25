// Created by none at 2025/11/25 12:50
// leetgo: dev
// https://leetcode.com/problems/smallest-integer-divisible-by-k/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func smallestRepunitDivByK(k int) int {
	if k&1 == 0 || k%10 == 5 {
		return -1
	}
	x := 1
	for i := 1; i <= k; i++ {
		if x%k == 0 {
			return i
		}
		x = (x*10 + 1) % k
	}
	return -1
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	k := Deserialize[int](ReadLine(stdin))
	ans := smallestRepunitDivByK(k)

	fmt.Println("\noutput:", Serialize(ans))
}
