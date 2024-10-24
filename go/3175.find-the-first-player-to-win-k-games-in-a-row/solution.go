// Created by none at 2024/10/24 21:09
// leetgo: 1.4.9
// https://leetcode.cn/problems/find-the-first-player-to-win-k-games-in-a-row/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func findWinningPlayer(skills []int, k int) int {
	win := -1
	x := 0

	for i, y := range skills {
		if y > skills[x] {
			x = i
			win = 1
		} else {
			win++
		}
		if win >= k {
			return x
		}
	}

	return x

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	skills := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := findWinningPlayer(skills, k)

	fmt.Println("\noutput:", Serialize(ans))
}
