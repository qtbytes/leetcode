// Created by none at 2025/09/19 11:47
// leetgo: dev
// https://leetcode.com/problems/design-spreadsheet/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

type Spreadsheet struct {
	board [][26]int
}

func Constructor(rows int) Spreadsheet {
	board := make([][26]int, rows)
	return Spreadsheet{board}
}

func parse(cell string) (int, int) {
	col := int(cell[0] - 'A')
	row, _ := strconv.Atoi(cell[1:])
	return row - 1, col
}

func (s *Spreadsheet) SetCell(cell string, value int) {
	row, col := parse(cell)
	s.board[row][col] = value
}

func (s *Spreadsheet) ResetCell(cell string) {
	row, col := parse(cell)
	s.board[row][col] = 0
}

func (s *Spreadsheet) GetValue(formula string) int {
	i := strings.Index(formula, "+")
	left, right := formula[1:i], formula[i+1:]
	res := 0
	for _, X := range [2]string{left, right} {
		if n, err := strconv.Atoi(X); err == nil {
			res += n
		} else {
			row, col := parse(X)
			res += s.board[row][col]
		}
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	ops := Deserialize[[]string](ReadLine(stdin))
	params := MustSplitArray(ReadLine(stdin))
	output := make([]string, 0, len(ops))
	output = append(output, "null")

	constructorParams := MustSplitArray(params[0])
	rows := Deserialize[int](constructorParams[0])
	obj := Constructor(rows)

	for i := 1; i < len(ops); i++ {
		switch ops[i] {
		case "setCell":
			methodParams := MustSplitArray(params[i])
			cell := Deserialize[string](methodParams[0])
			value := Deserialize[int](methodParams[1])
			obj.SetCell(cell, value)
			output = append(output, "null")
		case "resetCell":
			methodParams := MustSplitArray(params[i])
			cell := Deserialize[string](methodParams[0])
			obj.ResetCell(cell)
			output = append(output, "null")
		case "getValue":
			methodParams := MustSplitArray(params[i])
			formula := Deserialize[string](methodParams[0])
			ans := Serialize(obj.GetValue(formula))
			output = append(output, ans)
		}
	}
	fmt.Println("\noutput:", JoinArray(output))
}
