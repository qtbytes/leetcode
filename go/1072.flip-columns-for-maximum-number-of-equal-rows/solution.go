// Created by none at 2024/11/22 16:56
// leetgo: 1.4.9
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

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
func slice_to_string(s *[]int) string {
	var res []string
	for _, x := range *s {
		res = append(res, strconv.Itoa(x))
	}
	return strings.Join(res, " ")
}

func maxEqualRowsAfterFlips(matrix [][]int) int {
	cnt := make(map[string]int)
	for _, row := range matrix {
		group := make([][]int, 2)
		for j, x := range row {
			group[x&1] = append(group[x&1], j)
		}
		for _, g := range group {
			cnt[slice_to_string(&g)]++
		}
	}
	res := 0
	for _, c := range cnt {
		res = max(res, c)
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	matrix := Deserialize[[][]int](ReadLine(stdin))
	ans := maxEqualRowsAfterFlips(matrix)

	fmt.Println("\noutput:", Serialize(ans))
}
