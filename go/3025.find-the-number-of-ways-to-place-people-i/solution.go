// Created by none at 2025/09/02 10:10
// leetgo: dev
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func numberOfPairs(points [][]int) int {
	isUpperLeft := func(i, j int) bool {
		return points[i][1] >= points[j][1]
	}
	insideRec := func(k, i, j int) bool {
		return points[j][1] <= points[k][1] && points[k][1] <= points[i][1]
	}

	sort.Slice(points, func(i, j int) bool {
		return points[i][0] < points[j][0] || (points[i][0] == points[j][0] && points[i][1] > points[j][1])
	})
	n := len(points)
	res := 0
	for j := range n {
		for i := range j {
			if !isUpperLeft(i, j) {
				continue
			}
			ok := 1
			for k := i + 1; k < j; k++ {
				if insideRec(k, i, j) {
					ok = 0
					break
				}
			}
			// fmt.Println(i, j)
			res += ok
		}
	}

	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	points := Deserialize[[][]int](ReadLine(stdin))
	ans := numberOfPairs(points)

	fmt.Println("\noutput:", Serialize(ans))
}
