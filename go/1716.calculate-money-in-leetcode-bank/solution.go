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
	m, k := n/7, n%7
	return 7*(4+m-1+4)*m/2 + (m+1+m+k)*k/2
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	ans := totalMoney(n)

	fmt.Println("\noutput:", Serialize(ans))
}
