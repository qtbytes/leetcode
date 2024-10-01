// Created by none at 2024/10/01 14:41
// leetgo: 1.4.9
// https://leetcode.cn/problems/minimum-cost-for-tickets/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func mincostTickets(days []int, costs []int) int {
	/*
		f[i] = min(f[i-duration[i]]+cost[i])
	*/
	i, j, k := 0, 0, 0
	n := len(days)

	f := make([]int, n+1)

	for r, x := range days {
		for x-days[i] >= 1 {
			i++
		}
		for x-days[j] >= 7 {
			j++
		}
		for x-days[k] >= 30 {
			k++
		}
		f[r+1] = min(f[i]+costs[0], f[j]+costs[1], f[k]+costs[2])
	}
	return f[n]

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	days := Deserialize[[]int](ReadLine(stdin))
	costs := Deserialize[[]int](ReadLine(stdin))
	ans := mincostTickets(days, costs)

	fmt.Println("\noutput:", Serialize(ans))
}
