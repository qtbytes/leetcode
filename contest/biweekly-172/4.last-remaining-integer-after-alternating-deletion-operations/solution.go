// Created by none at 2025/12/22 21:14
// leetgo: dev
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/
// https://leetcode.com/contest/biweekly-contest-172/problems/last-remaining-integer-after-alternating-deletion-operations/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
func dfs(n int, left bool) int {
	if n == 1 {
		return 1
	}
	if left {
		return 2*(dfs((n+1)/2, !left)) - 1
	}
	return 2*dfs((n+1)/2, !left) - (n & 1)
}

func lastInteger(n int64) int64 {
	return int64(dfs(int(n), true))
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int64](ReadLine(stdin))
	ans := lastInteger(n)

	fmt.Println("\noutput:", Serialize(ans))
}
