// Created by none at 2024/10/09 12:47
// leetgo: 1.4.9
// https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

const N = 31

func minimumDifference(nums []int, k int) int {

	cnt := make([]int, N)

	ans := 0
	l := 0
	res := abs(nums[0] - k)
	for r, x := range nums {
		for i := range N {
			if x>>i&1 == 1 {
				cnt[i] += 1
				ans |= 1 << i
			}
		}
		res = min(res, abs(k-ans))

		for ans > k && l < r {
			x := nums[l]
			for i := range N {
				if x>>i&1 == 1 {
					cnt[i] -= 1
					if cnt[i] == 0 {
						ans ^= 1 << i
					}
				}
			}
			l += 1
			res = min(res, abs(k-ans))
		}
		if res == 0 {
			return 0
		}
	}

	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := minimumDifference(nums, k)

	fmt.Println("\noutput:", Serialize(ans))
}
