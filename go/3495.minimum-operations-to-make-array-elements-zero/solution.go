// Created by none at 2025/09/06 10:08
// leetgo: dev
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
func calc(l, r int) int {
	x, y := 0, 4
	t := 1
	res := 0
	for x <= r {
		// x .. l ... y .... r
		// fmt.Println(x, y, max(l, x), min(r, y-1))
		res += t * max(0, (min(r, y-1)-max(l, x)+1))
		x, y, t = y, 4*y, t+1
	}
	// fmt.Println(l, r, res)
	return (res + 1) / 2
}

func minOperations(queries [][]int) int64 {
	res := 0
	for _, q := range queries {
		l, r := q[0], q[1]
		res += calc(l, r)
	}
	return int64(res)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	queries := Deserialize[[][]int](ReadLine(stdin))
	ans := minOperations(queries)

	fmt.Println("\noutput:", Serialize(ans))
}
