// Created by none at 2025/12/31 12:56
// leetgo: dev
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func latestDayToCross(row int, col int, cells [][]int) int {
	fa := make([]int, row*col)
	for i := range fa {
		fa[i] = i
	}

	var find func(x int) int
	find = func(x int) int {
		if fa[x] != x {
			fa[x] = find(fa[x])
		}
		return fa[x]
	}

	union := func(x, y int) bool {
		fx, fy := find(x), find(y)
		if fx != fy {
			fa[fy] = fx
			return true
		}
		return false
	}

	for i := range row - 1 {
		union(i*col, (i+1)*col)
		union(i*col+col-1, (i+1)*col+col-1)
	}

	seen := map[[2]int]struct{}{}

	for day, cell := range cells {
		x, y := cell[0]-1, cell[1]-1
		for dx := range 3 {
			for dy := range 3 {
				nx, ny := x+dx-1, y+dy-1
				if x == nx && y == ny {
					continue
				}
				if _, ok := seen[[2]int{nx, ny}]; ok {
					union(x*col+y, nx*col+ny)
					if find(0) == find(row*col-1) {
						return day
					}
				}
			}
		}
		seen[[2]int{x, y}] = struct{}{}
	}
	return -1
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	row := Deserialize[int](ReadLine(stdin))
	col := Deserialize[int](ReadLine(stdin))
	cells := Deserialize[[][]int](ReadLine(stdin))
	ans := latestDayToCross(row, col, cells)

	fmt.Println("\noutput:", Serialize(ans))
}
