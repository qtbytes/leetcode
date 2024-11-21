// Created by none at 2024/11/21 14:08
// leetgo: 1.4.9
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	grid := make([][]int, m)
	for i := range grid {
		grid[i] = make([]int, n)
	}
	for _, g := range guards {
		grid[g[0]][g[1]] = 1
	}
	for _, w := range walls {
		grid[w[0]][w[1]] = 2
	}
	var dfs func(x, y, dx, dy int)
	dfs = func(x, y, dx, dy int) {
		x += dx
		y += dy
		if x < 0 || x >= m || y < 0 || y >= n {
			return
		}
		if grid[x][y] == 1 || grid[x][y] == 2 {
			return
		}
		grid[x][y] = 3
		dfs(x, y, dx, dy)
	}

	dirs := []int{0, 1, 0, -1, 0}
	for _, g := range guards {
		x, y := g[0], g[1]
		for d := range len(dirs) - 1 {
			dfs(x, y, dirs[d], dirs[d+1])
		}
	}
	fmt.Println(grid)
	ans := 0
	for _, row := range grid {
		for _, x := range row {
			if x == 0 {
				ans++
			}
		}
	}
	return ans

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	m := Deserialize[int](ReadLine(stdin))
	n := Deserialize[int](ReadLine(stdin))
	guards := Deserialize[[][]int](ReadLine(stdin))
	walls := Deserialize[[][]int](ReadLine(stdin))
	ans := countUnguarded(m, n, guards, walls)

	fmt.Println("\noutput:", Serialize(ans))
}
