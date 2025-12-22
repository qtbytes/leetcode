// Created by none at 2025/12/22 21:14
// leetgo: dev
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/
// https://leetcode.com/contest/biweekly-contest-172/problems/maximum-sum-of-three-numbers-divisible-by-three/

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

func maximumSum(nums []int) int {
	// 0 0 0
	// 0 1 2
	// 1 1 1
	// 2 2 2
	//
	a := [3][]int{}
	for _, x := range nums {
		a[x%3] = append(a[x%3], x)
	}

	ans := 0
	for i := range a {
		sort.Ints(a[i])
		slices.Reverse(a[i])
		a[i] = a[i][:min(3, len(a[i]))]
		if len(a[i]) >= 3 {
			ans = max(ans, a[i][0]+a[i][1]+a[i][2])
		}
	}

	if len(a[0]) > 0 && len(a[1]) > 0 && len(a[2]) > 0 {
		ans = max(ans, a[0][0]+a[1][0]+a[2][0])
	}

	return ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := maximumSum(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
