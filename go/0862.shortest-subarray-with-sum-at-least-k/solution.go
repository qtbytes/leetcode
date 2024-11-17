// Created by none at 2024/11/17 13:54
// leetgo: 1.4.9
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func shortestSubarray(nums []int, k int) int {
	if slices.Max(nums) >= k {
		return 1
	}
	n := len(nums)
	res := math.MaxInt
	s := make([]int, n+1)
	q := []int{0}
	for i, x := range nums {
		s[i+1] = s[i] + x
		for len(q) > 1 && s[i+1] <= s[q[len(q)-1]] {
			q = q[:len(q)-1]
		}
		target := s[i+1] - k
		if len(q) > 0 {
			j := sort.Search(len(q), func(i int) bool {
				return s[q[i]] > target
			})
			if j > 0 {
				res = min(res, i-q[j-1]+1)
			}
		}
		q = append(q, i+1)
	}
	if res == math.MaxInt {
		return -1
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := shortestSubarray(nums, k)

	fmt.Println("\noutput:", Serialize(ans))
}
