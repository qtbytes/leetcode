// Created by none at 2024/11/28 13:24
// leetgo: 1.4.9
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
const INF int = 1e9

var DIRS = []int{0, 1, 0, -1, 0}

type Pair struct {
	x, y int
}

func minimumObstacles(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	visited := make([][]int, m)
	for i := range visited {
		visited[i] = make([]int, n)
	}
	for i, row := range grid {
		for j, x := range row {
			if x == 1 {
				grid[i][j] = INF
			}
		}
	}
	q := list.New()
	q.PushBack(Pair{0, 0})
	visited[0][0] = 1
	for q.Len() > 0 {
		// fmt.Println(q)
		p := q.Remove(q.Front()).(Pair)
		if p.x == m-1 && p.y == n-1 {
			return grid[p.x][p.y]
		}
		for i := range 4 {
			dx, dy := DIRS[i], DIRS[i+1]
			x, y := p.x+dx, p.y+dy
			if 0 <= x && x < m && 0 <= y && y < n && visited[x][y] == 0 {
				visited[x][y] = 1
				if grid[x][y] > grid[p.x][p.y]+1 {
					grid[x][y] = grid[p.x][p.y] + 1
					q.PushBack(Pair{x, y})
				} else if grid[x][y] == 0 {
					grid[x][y] = grid[p.x][p.y]
					q.PushFront(Pair{x, y})
				}
			}
		}
	}
	return grid[m-1][n-1]
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	grid := Deserialize[[][]int](ReadLine(stdin))
	ans := minimumObstacles(grid)

	fmt.Println("\noutput:", Serialize(ans))
}
