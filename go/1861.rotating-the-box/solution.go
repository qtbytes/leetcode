// Created by none at 2024/11/23 13:57
// leetgo: 1.4.9
// https://leetcode.com/problems/rotating-the-box/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func rotateTheBox(box [][]byte) [][]byte {
	m, n := len(box), len(box[0])
	ans := make([][]byte, n)
	for i := range n {
		ans[i] = make([]byte, m)
	}
	for i, row := range box {
		for j, ch := range row {
			ans[j][m-1-i] = ch
		}
	}
	// optimize drop: cnt stones
	// rearrange the stones if meet wall
	var drop func(x, y int)
	drop = func(x int, y int) {
		/// stone(x, y) drop
		if x+1 < n && ans[x+1][y] == '#' {
			drop(x+1, y)
		}
		if x+1 < n && ans[x+1][y] == '.' {
			ans[x+1][y], ans[x][y] = ans[x][y], ans[x+1][y]
			drop(x+1, y)
		}
	}
	for i, row := range ans {
		for j, ch := range row {
			if ch == '#' {
				drop(i, j)
			}
		}
	}

	return ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	box := Deserialize[[][]byte](ReadLine(stdin))
	ans := rotateTheBox(box)

	fmt.Println("\noutput:", Serialize(ans))
}
