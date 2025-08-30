// Created by none at 2025/08/30 11:27
// leetgo: dev
// https://leetcode.com/problems/valid-sudoku/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func isValidSudoku(board [][]byte) bool {
	// fmt.Println(board)
	// n := len(board)
	// rows := make([][]bool, n)
	// cols := make([][]bool, n)
	// for i := range n {
	// 	rows[i] = make([]bool, n)
	// 	cols[i] = make([]bool, n)
	// }
	// // fmt.Println(rows, cols)
	// grid := make([][][]bool, 3)
	// for i := range grid {
	// 	grid[i] = make([][]bool, 3)
	// 	for j := range grid[i] {
	// 		grid[i][j] = make([]bool, n)
	// 	}
	// }
	// fmt.Println(grid)

	rows := [9][9]bool{}
	cols := [9][9]bool{}
	grid := [3][3][9]bool{}

	for i, row := range board {
		for j, ch := range row {
			if ch == byte('.') {
				continue
			}
			x := ch - byte('1')
			if rows[i][x] || cols[j][x] || grid[i/3][j/3][x] {
				return false
			}
			rows[i][x] = true
			cols[j][x] = true
			grid[i/3][j/3][x] = true

		}
	}

	return true
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	board := Deserialize[[][]byte](ReadLine(stdin))
	ans := isValidSudoku(board)

	fmt.Println("\noutput:", Serialize(ans))
}
