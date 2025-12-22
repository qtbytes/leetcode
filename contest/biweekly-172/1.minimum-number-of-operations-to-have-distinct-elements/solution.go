// Created by none at 2025/12/22 21:14
// leetgo: dev
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/
// https://leetcode.com/contest/biweekly-contest-172/problems/minimum-number-of-operations-to-have-distinct-elements/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func minOperations(nums []int) int {
	freq := map[int]int{}
	cnt := 0

	for _, x := range nums {
		freq[x]++
		if freq[x] == 2 {
			cnt++
		}
	}

	ans := 0
	i := 0
	n := len(nums)
	for cnt > 0 {
		ans++
		for j := range 3 {
			if i+j >= n {
				break
			}
			x := nums[i+j]
			freq[x]--
			if freq[x] == 1 {
				cnt--
			}
		}
		i += 3
	}

	return ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := minOperations(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
