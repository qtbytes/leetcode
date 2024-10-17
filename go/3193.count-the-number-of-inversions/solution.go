// Created by none at 2024/10/17 11:55
// leetgo: 1.4.9
// https://leetcode.cn/problems/count-the-number-of-inversions/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

const MOD = int(1e9) + 7

func numberOfPermutations(n int, requirements [][]int) int {

	rn := make(map[int]int) // reversion needed
	for i := range n + 1 {
		rn[i] = -1
	}
	for _, r := range requirements {
		rn[r[0]+1] = r[1]
	}
	if rn[n] == 0 {
		return 1
	}

	memo := make([][]int, n+1)
	for i := range n + 1 {
		memo[i] = make([]int, rn[n]+1)
		for j := range rn[n] + 1 {
			memo[i][j] = -1
		}
	}

	var dfs func(n, rc int) int // rc: reversion count
	dfs = func(n, rc int) int {
		if rc < 0 || (rn[n] != -1 && rc != rn[n]) {
			return 0
		}
		if n == 0 && rc == 0 {
			return 1
		}
		if memo[n][rc] != -1 {
			return memo[n][rc]
		}
		res := 0
		for x := range n {
			res += dfs(n-1, rc-x)
		}
		memo[n][rc] = res % MOD
		return res % MOD
	}

	return dfs(n, rn[n])

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	requirements := Deserialize[[][]int](ReadLine(stdin))
	ans := numberOfPermutations(n, requirements)

	fmt.Println("\noutput:", Serialize(ans))
}
