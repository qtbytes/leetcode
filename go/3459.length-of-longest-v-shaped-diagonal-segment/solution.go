// Created by none at 2025/08/27 10:24
// leetgo: dev
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type Item struct {
	i, j    int
	dx, dy  int
	canTurn bool
}

type Dir struct {
	dx, dy int
}

func lenOfVDiagonal(grid [][]int) int {
	m, n := len(grid), len(grid[0])

	memo := make(map[Item]int)
	next := [3]int{2, 2, 0}

	valid := func(i, j int) bool {
		return !(i >= m || i < 0 || j < 0 || j >= n)
	}

	var dfs func(i, j int, dx, dy int, canTurn bool) int
	dfs = func(i, j, dx, dy int, canTurn bool) int {
		if !valid(i, j) {
			return 0
		}
		item := Item{i, j, dx, dy, canTurn}
		if res, ok := memo[item]; ok {
			return res
		}
		res := 0
		// don't turn
		x, y := i+dx, j+dy
		if valid(x, y) && grid[x][y] == next[grid[i][j]] {
			res = 1 + dfs(x, y, dx, dy, canTurn)
		}
		// turn
		dx, dy = dy, -dx
		x, y = i+dx, j+dy
		if canTurn && valid(x, y) && grid[x][y] == next[grid[i][j]] {
			res = max(res, 1+dfs(x, y, dx, dy, false))
		}
		memo[item] = res
		return res
	}

	res := 0

	for i, row := range grid {
		for j, x := range row {
			if x == 1 {
				dirs := [4]Dir{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
				max_step := [4]int{m - i, j + 1, n - j, i + 1}
				for k, d := range dirs {
					if max_step[k] > res {
						res = max(res, 1+dfs(i, j, d.dx, d.dy, true))
					}
				}
			}
		}
	}

	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	grid := Deserialize[[][]int](ReadLine(stdin))
	ans := lenOfVDiagonal(grid)

	fmt.Println("\noutput:", Serialize(ans))
}
