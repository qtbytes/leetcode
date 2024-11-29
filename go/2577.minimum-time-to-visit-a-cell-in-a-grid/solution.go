// Created by none at 2024/11/29 13:36
// leetgo: 1.4.9
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type hp []Pair

func (h *hp) Len() int {
	return len(*h)
}
func (h *hp) Less(i, j int) bool {
	return (*h)[i].d < (*h)[j].d
}
func (h *hp) Swap(i, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}
func (h *hp) Push(x any) {
	(*h) = append(*h, x.(Pair))
}
func (h *hp) Pop() any {
	n := len(*h)
	x := (*h)[n-1]
	*h = (*h)[:n-1]
	return x
}

var dirs = [5]int{0, 1, 0, -1, 0}

type Pair struct {
	d    int
	x, y int
}

const INF int = 1e9

func minimumTime(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	if grid[0][1] > 1 && grid[1][0] > 1 {
		return -1
	}
	visit := make([][]int, m)
	for i := range visit {
		visit[i] = make([]int, n)
		for j := range visit[i] {
			visit[i][j] = INF
		}
	}
	q := &hp{}
	heap.Push(q, Pair{0, 0, 0})
	visit[0][0] = 0
	for q.Len() > 0 {
		p := heap.Pop(q).(Pair)
		if p.d != visit[p.x][p.y] {
			continue
		}
		for i := range 4 {
			dx, dy := dirs[i], dirs[i+1]
			x, y := p.x+dx, p.y+dy
			if 0 <= x && x < m && 0 <= y && y < n {
				var d int
				if grid[x][y] <= p.d+1 {
					d = p.d + 1
				} else {
					d = grid[x][y]
					if grid[x][y]&1 != (p.d+1)&1 {
						d++
					}
				}
				if d < visit[x][y] {
					visit[x][y] = d
					heap.Push(q, Pair{d, x, y})
				}
			}
		}
	}

	return visit[m-1][n-1]

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	grid := Deserialize[[][]int](ReadLine(stdin))
	ans := minimumTime(grid)

	fmt.Println("\noutput:", Serialize(ans))
}
