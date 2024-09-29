// Created by none at 2024/09/29 11:51
// leetgo: 1.4.9
// https://leetcode.cn/problems/time-needed-to-buy-tickets/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func timeRequiredToBuy(tickets []int, k int) int {
	res := 0
	for i, x := range tickets {
		if i <= k {
			res += min(tickets[k], x)
		} else {
			res += min(tickets[k]-1, x)
		}
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	tickets := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := timeRequiredToBuy(tickets, k)

	fmt.Println("\noutput:", Serialize(ans))
}
