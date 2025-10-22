// Created by none at 2025/10/22 11:18
// leetgo: dev
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maxFrequency(nums []int, k int, numOperations int) int {
	var keys []int
	cnt := make(map[int]int)
	for _, x := range nums {
		keys = append(keys, x, x-k)
		cnt[x]++
	}

	sort.Ints(nums)
	res := 0
	for _, key := range keys {
		l := sort.Search(len(nums), func(i int) bool { return nums[i]+k >= key })
		r := sort.Search(len(nums), func(i int) bool { return nums[i]-k > key })
		res = max(res, min(r-l, cnt[key]+numOperations))
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	numOperations := Deserialize[int](ReadLine(stdin))
	ans := maxFrequency(nums, k, numOperations)

	fmt.Println("\noutput:", Serialize(ans))
}
