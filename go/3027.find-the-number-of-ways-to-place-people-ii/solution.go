// Created by none at 2025/09/03 12:24
// leetgo: dev
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

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
	sort.Slice(points, func(i, j int) bool {
		return points[i][0] < points[j][0] || (points[i][0] == points[j][0] && points[i][1] > points[j][1])
	})
	res := 0
	n := len(points)

	for i := range n {
		y := points[i][1]
		max_height := int(-2e9) // the highest point less then y
		for j := i + 1; j < n; j++ {
			if points[j][1] > y {
				continue
			}
			if points[j][1] > max_height {
				res++
				max_height = points[j][1]
			}
			if max_height == y {
				break
			}
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
