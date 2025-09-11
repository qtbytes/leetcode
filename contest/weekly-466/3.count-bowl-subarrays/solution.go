// Created by none at 2025/09/10 22:27
// leetgo: dev
// https://leetcode.com/problems/count-bowl-subarrays/
// https://leetcode.com/contest/weekly-contest-466/problems/count-bowl-subarrays/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func bowlSubarrays(nums []int) int64 {
	res := 0
	var st []int
	for _, x := range nums {
		if len(st) > 0 && st[len(st)-1] < x {
			i := sort.Search(len(st), func(i int) bool { return st[i] < x })
			// we can use i-1..=n-2 as left
			res += len(st) - 1 - max(i-1, 0)
		}
		for len(st) > 0 && x >= st[len(st)-1] {
			st = st[:len(st)-1]
		}
		st = append(st, x)
	}
	return int64(res)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := bowlSubarrays(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
