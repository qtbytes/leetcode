// Created by none at 2025/12/01 12:03
// leetgo: dev
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

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

func maxRunTime(n int, batteries []int) int64 {
	s := 0
	for _, x := range batteries {
		s += x
	}
	l, r := 0, s/n+1

	sort.Ints(batteries)
	slices.Reverse(batteries)

	check := func(mid int) bool {
		cnt := 0
		last := 0
		for _, x := range batteries {
			last += x
			if last >= mid {
				cnt += 1
				if x >= mid {
					last = 0
				} else {
					last -= mid
				}
			}
		}
		return cnt >= n
	}

	for l < r {
		mid := (l + r + 1) >> 1
		if check(mid) {
			l = mid
		} else {
			r = mid - 1
		}
	}
	return int64(l)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	batteries := Deserialize[[]int](ReadLine(stdin))
	ans := maxRunTime(n, batteries)

	fmt.Println("\noutput:", Serialize(ans))
}
