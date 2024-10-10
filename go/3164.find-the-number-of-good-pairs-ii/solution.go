// Created by none at 2024/10/10 11:45
// leetgo: 1.4.9
// https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
const N = int(1e6) + 1

func numberOfPairs(nums1 []int, nums2 []int, k int) int64 {
	cnt := make(map[int]int)
	for _, x := range nums2 {
		cnt[x] += 1
	}
	res := 0

	for _, x := range nums1 {
		if x%k != 0 {
			continue
		}
		x /= k
		// find y (x % y ==0)
		for y := 1; y*y <= x; y++ {
			if x%y == 0 {
				// fmt.Println(x, y)
				res += cnt[y]
				if x/y != y {
					res += cnt[x/y]
				}
			}
		}

	}

	return int64(res)

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums1 := Deserialize[[]int](ReadLine(stdin))
	nums2 := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := numberOfPairs(nums1, nums2, k)

	fmt.Println("\noutput:", Serialize(ans))
}
