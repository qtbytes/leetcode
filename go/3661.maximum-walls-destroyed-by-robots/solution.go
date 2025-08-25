// Created by none at 2025/08/25 23:59
// leetgo: dev
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type Robot struct {
	x int
	r int
}

func maxWalls(pos []int, distance []int, walls []int) int {
	sort.Ints(walls)
	robots := make([]Robot, 0)
	for i, x := range pos {
		robots = append(robots, Robot{x, distance[i]})
	}

	sort.Slice(robots, func(i, j int) bool {
		return robots[i].x < robots[j].x
	})

	m := len(robots)
	n := len(walls)

	memo := make([][2]int, m)
	for i := range memo {
		memo[i] = [2]int{-1, -1}
	}

	var dfs func(i int, canShotLast int) int
	dfs = func(i int, canShotLast int) int {
		if i == m {
			return 0
		}
		p := &memo[i][canShotLast]
		if *p != -1 {
			return *p
		}
		x := robots[i].x
		res := 0
		// left
		left := robots[i].x - robots[i].r
		if i > 0 {
			if canShotLast == 0 {
				left = max(left, robots[i-1].x+robots[i-1].r+1)
			} else {
				left = max(left, robots[i-1].x+1)
			}
		}
		l := sort.Search(n, func(i int) bool { return walls[i] >= left })
		r := sort.Search(n, func(i int) bool { return walls[i] > x })
		res = r - l + dfs(i+1, 1)
		// right
		right := robots[i].x + robots[i].r
		if i < m-1 {
			right = min(right, robots[i+1].x-1)
		}
		l = sort.Search(n, func(i int) bool { return walls[i] >= x })
		r = sort.Search(n, func(i int) bool { return walls[i] > right })
		res = max(res, r-l+dfs(i+1, 0))
		*p = res
		return res
	}

	return dfs(0, 1)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	robots := Deserialize[[]int](ReadLine(stdin))
	distance := Deserialize[[]int](ReadLine(stdin))
	walls := Deserialize[[]int](ReadLine(stdin))
	ans := maxWalls(robots, distance, walls)

	fmt.Println("\noutput:", Serialize(ans))
}
