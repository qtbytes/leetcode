// Created by none at 2025/08/31 11:35
// leetgo: dev
// https://leetcode.com/problems/sudoku-solver/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func solveSudoku(board [][]byte) {
	rows := [9][9]bool{}
	cols := [9][9]bool{}
	grid := [3][3][9]bool{}
	// enumerate board

	for i, row := range board {
		for j, ch := range row {
			if ch == '.' {
				continue
			}
			x := ch - '1'
			rows[i][x] = true
			cols[j][x] = true
			grid[i/3][j/3][x] = true
		}
	}

	var dfs func(x, y int) bool
	dfs = func(x, y int) bool {
		if y >= 9 {
			x, y = x+1, 0
		}
		if x >= 9 {
			return true
		}
		if board[x][y] != '.' {
			return dfs(x, y+1)
		}

		// try fill cell [x, y] with number i
		for i := range 9 {
			if rows[x][i] || cols[y][i] || grid[x/3][y/3][i] {
			} else {
				board[x][y] = byte(i) + '1'
				rows[x][i] = true
				cols[y][i] = true
				grid[x/3][y/3][i] = true
				if dfs(x, y+1) {
					return true
				}
				board[x][y] = '.'
				rows[x][i] = false
				cols[y][i] = false
				grid[x/3][y/3][i] = false
			}
		}

		return false
	}
	// dfs(0, 0)
	// fmt.Println(board)
	fmt.Println(dfs(0, 0))
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	board := Deserialize[[][]byte](ReadLine(stdin))
	solveSudoku(board)
	ans := board

	fmt.Println("\noutput:", Serialize(ans))
}
