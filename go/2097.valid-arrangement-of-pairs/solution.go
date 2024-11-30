// Created by none at 2024/11/30 14:07
// leetgo: 1.4.9
// https://leetcode.com/problems/valid-arrangement-of-pairs/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func validArrangement(pairs [][]int) [][]int {
	deg := make(map[int]int)
	g := make(map[int][]int)
	for _, p := range pairs {
		x, y := p[0], p[1]
		deg[x]++
		deg[y]--
		g[x] = append(g[x], y)
	}
	start := []int{}
	for k, v := range deg {
		if v == 1 {
			start = append(start, k)
		}
	}
	res := [][]int{}

	var x int
	if len(start) == 1 {
		x = start[0]
	} else {
		x = pairs[0][0]
	}

	var dfs func(x int)
	dfs = func(x int) {
		for len(g[x]) > 0 {
			y := g[x][0]
			g[x] = g[x][1:]
			dfs(y)
			res = append(res, []int{x, y})
		}
	}

	dfs(x)
	slices.Reverse(res)
	return res

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	pairs := Deserialize[[][]int](ReadLine(stdin))
	ans := validArrangement(pairs)

	fmt.Println("\noutput:", Serialize(ans))
}
