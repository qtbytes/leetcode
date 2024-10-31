// Created by none at 2024/10/31 14:15
// leetgo: 1.4.9
// https://leetcode.com/problems/minimum-total-distance-traveled/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
func minimumTotalDistance(robot []int, factory [][]int) int64 {
	pos := make([]int, 0, 10000)
	for _, f := range factory {
		for i := 0; i < f[1]; i++ {
			pos = append(pos, f[0])
		}
	}

	n := len(robot)
	m := len(pos)

	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, m+1)
	}

	sort.Ints(robot)
	sort.Ints(pos)
	for i, r := range robot {
		dp[i+1][i+1] = dp[i][i] + abs(r-pos[i])
		for j := i + 1; j < m; j++ {
			p := pos[j]
			dp[i+1][j+1] = min(dp[i+1][j], dp[i][j]+abs(r-p))
		}
	}
	return int64(dp[n][m])

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	robot := Deserialize[[]int](ReadLine(stdin))
	factory := Deserialize[[][]int](ReadLine(stdin))
	ans := minimumTotalDistance(robot, factory)

	fmt.Println("\noutput:", Serialize(ans))
}
