// Created by none at 2025/10/25 09:10
// leetgo: dev
// https://leetcode.com/problems/calculate-money-in-leetcode-bank/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func totalMoney(n int) int {
	m := n / 7
	weekMoney := (1 + 7) * 7 / 2
	res := 0
	for range m {
		res += weekMoney
		weekMoney += 7
	}
	for range n - m*7 {
		m++
		res += m
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	ans := totalMoney(n)

	fmt.Println("\noutput:", Serialize(ans))
}
