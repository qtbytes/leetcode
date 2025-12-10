// Created by none at 2025/12/10 16:38
// leetgo: dev
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func countPermutations(complexity []int) int {
	first := complexity[0]
	mod := int(1e9) + 7
	n := len(complexity)
	ans := 1
	for i := 1; i < n; i++ {
		if complexity[i] <= first {
			return 0
		}
		ans = (ans * i) % mod
	}
	return ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	complexity := Deserialize[[]int](ReadLine(stdin))
	ans := countPermutations(complexity)

	fmt.Println("\noutput:", Serialize(ans))
}
