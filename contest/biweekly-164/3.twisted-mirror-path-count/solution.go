// Created by none at 2025/09/11 20:52
// leetgo: dev
// https://leetcode.com/problems/twisted-mirror-path-count/
// https://leetcode.com/contest/biweekly-contest-164/problems/twisted-mirror-path-count/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type dir struct {
	dx, dy int
}

const mod int = 1e9 + 7

func uniquePaths(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dirs := [2]dir{{0, 1}, {1, 0}}

	memo := make([][][4]int, m)
	for i := range memo {
		memo[i] = make([][4]int, n)
		for j := range memo[i] {
			memo[i][j] = [4]int{-1, -1, -1, -1}
		}
	}
	invalid := func(i, j int) bool {
		return (i < 0 || i >= m || j < 0 || j >= n)
	}
	var dfs func(i, j, d int) int
	dfs = func(i, j, d int) int {
		// fmt.Println(i, j, d)
		if invalid(i, j) {
			return 0
		}
		if i == m-1 && j == n-1 {
			return 1
		}
		if grid[i][j] == 0 {
			d = 0b11
		} else {
			d ^= 0b11 // mirror
		}
		// fmt.Println(i, j, d)
		p := &memo[i][j][d]
		if *p != -1 {
			return *p
		}
		*p = 0 // tag visited
		res := 0
		for k, dir := range dirs {
			if d>>k&1 == 1 {
				res += dfs(i+dir.dx, j+dir.dy, 1<<k)
			}
		}
		*p = res % mod
		// fmt.Println(i, j, *p)
		return *p
	}
	return dfs(0, 0, 0b11)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	grid := Deserialize[[][]int](ReadLine(stdin))
	ans := uniquePaths(grid)

	fmt.Println("\noutput:", Serialize(ans))
}
