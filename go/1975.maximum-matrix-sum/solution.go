// Created by none at 2024/11/24 14:21
// leetgo: 1.4.9
// https://leetcode.com/problems/maximum-matrix-sum/

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maxMatrixSum(matrix [][]int) int64 {
	ans := 0
	cnt := 0 // cnt neg
	has_zero := false
	y := math.MaxInt32
	for _, row := range matrix {
		for _, x := range row {
			if x > 0 {
				y = min(y, x)
				ans += x
			} else if x < 0 {
				y = min(y, -x)
				ans -= x
				cnt++
			} else {
				has_zero = true
			}
		}
	}

	if !has_zero && cnt&1 == 1 {
		ans -= 2 * y
	}
	return int64(ans)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	matrix := Deserialize[[][]int](ReadLine(stdin))
	ans := maxMatrixSum(matrix)

	fmt.Println("\noutput:", Serialize(ans))
}
