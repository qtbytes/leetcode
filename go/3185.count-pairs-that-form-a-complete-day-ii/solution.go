// Created by none at 2024/10/22 16:59
// leetgo: 1.4.9
// https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func countCompleteDayPairs(hours []int) int64 {
	cnt := make([]int, 24)
	res := 0
	for _, h := range hours {
		h %= 24
		res += cnt[(24-h)%24]
		cnt[h]++
	}
	return int64(res)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	hours := Deserialize[[]int](ReadLine(stdin))
	ans := countCompleteDayPairs(hours)

	fmt.Println("\noutput:", Serialize(ans))
}
