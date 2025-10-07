// Created by none at 2025/10/07 13:56
// leetgo: dev
// https://leetcode.com/problems/avoid-flood-in-the-city/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func avoidFlood(rains []int) []int {
	var canDry []int
	res := make([]int, len(rains))

	for i := range res {
		res[i] = -1
	}

	hasWater := make(map[int]int)

	for i, x := range rains {
		if x > 0 {
			if j, ok := hasWater[x]; ok {
				// find the first index canDry[k] > j
				k := sort.Search(len(canDry), func(i int) bool { return canDry[i] > j })
				if k < len(canDry) {
					res[canDry[k]] = x
					canDry = append(canDry[:k], canDry[k+1:]...)
				} else {
					return []int{}
				}
			}
			hasWater[x] = i
		} else {
			canDry = append(canDry, i)
		}
	}

	for _, i := range canDry {
		res[i] = 1
	}

	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	rains := Deserialize[[]int](ReadLine(stdin))
	ans := avoidFlood(rains)

	fmt.Println("\noutput:", Serialize(ans))
}
