// Created by none at 2024/10/30 12:34
// leetgo: 1.4.9
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

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

func minimumMountainRemovals(nums []int) int {
	n := len(nums)
	f := func(*[]int) []int {
		left := make([]int, n)
		// lcs
		q := []int{}
		for i, x := range nums {
			if len(q) == 0 || x > q[len(q)-1] {
				q = append(q, x)
				left[i] = i + 1 - len(q)
			} else {
				j := sort.Search(len(q), func(i int) bool { return x <= q[i] })
				q[j] = x
				left[i] = i - j
			}
		}
		return left
	}
	left := f(&nums)
	slices.Reverse(nums)
	right := f(&nums)
	slices.Reverse(right)
	res := n
	for i := 1; i < n-1; i++ {
		if i > left[i] && n-1-i > right[i] {
			res = min(res, left[i]+right[i])
		}
	}
	// fmt.Println(left, right)
	return res

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := minimumMountainRemovals(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
