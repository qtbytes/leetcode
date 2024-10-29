// Created by none at 2024/10/29 13:02
// leetgo: 1.4.9
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maxMoves(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	f := make([]int, m)
	res := 0
	for j := 1; j < n; j++ {
		f_next := make([]int, m)
		for i := range m {
			for k := -1; k <= 1; k++ {
				if i+k >= 0 && i+k < m && grid[i][j] > grid[i+k][j-1] && (j == 1 || f[i+k] != 0) {
					f_next[i] = max(f_next[i], 1+f[i+k])
				}
			}
		}
		f = f_next
		res = max(res, slices.Max(f))
		if res == 0 {
			break
		}
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	grid := Deserialize[[][]int](ReadLine(stdin))
	ans := maxMoves(grid)

	fmt.Println("\noutput:", Serialize(ans))
}
