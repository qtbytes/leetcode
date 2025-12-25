// Created by none at 2025/12/25 12:10
// leetgo: dev
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maximumHappinessSum(happiness []int, k int) int64 {
	sort.Ints(happiness)
	slices.Reverse(happiness)

	ans := 0
	for i := range k {
		ans += max(0, happiness[i]-i)
	}

	return int64(ans)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	happiness := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := maximumHappinessSum(happiness, k)

	fmt.Println("\noutput:", Serialize(ans))
}
