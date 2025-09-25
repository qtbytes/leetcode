// Created by none at 2025/09/25 10:05
// leetgo: dev
// https://leetcode.com/problems/triangle/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func minimumTotal(triangle [][]int) int {
	n := len(triangle)
	for i := n - 2; i >= 0; i-- {
		for j := range i + 1 {
			triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
		}
	}
	return triangle[0][0]
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	triangle := Deserialize[[][]int](ReadLine(stdin))
	ans := minimumTotal(triangle)

	fmt.Println("\noutput:", Serialize(ans))
}
