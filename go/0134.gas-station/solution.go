// Created by none at 2024/10/06 13:09
// leetgo: 1.4.9
// https://leetcode.cn/problems/gas-station/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func canCompleteCircuit(gas []int, cost []int) int {
	var s, j int
	min_s := gas[0] - cost[0]
	for i := range gas {
		s += gas[i] - cost[i]
		if s < min_s {
			min_s, j = s, i
		}
	}
	if s < 0 {
		return -1
	}
	return (j + 1) % len(gas)

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	gas := Deserialize[[]int](ReadLine(stdin))
	cost := Deserialize[[]int](ReadLine(stdin))
	ans := canCompleteCircuit(gas, cost)

	fmt.Println("\noutput:", Serialize(ans))
}
