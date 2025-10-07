// Created by none at 2025/10/07 13:56
// leetgo: dev
// https://leetcode.com/problems/avoid-flood-in-the-city/

package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/emirpasic/gods/v2/trees/redblacktree"
	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func avoidFlood(rains []int) []int {
	canDry := redblacktree.New[int, bool]()

	res := make([]int, len(rains))

	for i := range res {
		res[i] = -1
	}

	hasWater := make(map[int]int)

	for i, x := range rains {
		if x > 0 {
			if j, ok := hasWater[x]; ok {
				// find the first index canDry[k] > j
				k, ok := canDry.Ceiling(j)
				if ok {
					res[k.Key] = x
					canDry.Remove(k.Key)
				} else {
					return []int{}
				}
			}
			hasWater[x] = i
		} else {
			canDry.Put(i, true)
		}
	}

	for _, i := range canDry.Keys() {
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
