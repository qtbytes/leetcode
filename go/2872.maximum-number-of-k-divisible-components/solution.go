// Created by none at 2025/11/28 12:34
// leetgo: dev
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
	g := make([][]int, n)
	for _, e := range edges {
		x, y := e[0], e[1]
		g[x] = append(g[x], y)
		g[y] = append(g[y], x)
	}

	res := 0

	var dfs func(x, fa int) int
	dfs = func(x, fa int) int {
		score := values[x]
		for _, y := range g[x] {
			if y == fa {
				continue
			}
			score += dfs(y, x)
		}
		if score%k == 0 {
			res++
		}
		return score % k
	}
	dfs(0, -1)
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	edges := Deserialize[[][]int](ReadLine(stdin))
	values := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := maxKDivisibleComponents(n, edges, values, k)

	fmt.Println("\noutput:", Serialize(ans))
}
