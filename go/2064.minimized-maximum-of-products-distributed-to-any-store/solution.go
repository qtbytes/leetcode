// Created by none at 2024/11/14 12:46
// leetgo: 1.4.9
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func minimizedMaximum(n int, quantities []int) int {
	l, r := 1, slices.Max(quantities)
	check := func(mid int) bool {
		cnt := 0
		for _, x := range quantities {
			cnt += (x + mid - 1) / mid
		}
		return cnt <= n
	}
	for l < r {
		mid := (l + r) >> 1
		if !check(mid) {
			l = mid + 1
		} else {
			r = mid
		}
	}
	return l
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	quantities := Deserialize[[]int](ReadLine(stdin))
	ans := minimizedMaximum(n, quantities)

	fmt.Println("\noutput:", Serialize(ans))
}
