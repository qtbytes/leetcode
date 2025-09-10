// Created by none at 2025/09/10 09:51
// leetgo: dev
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
	m := len(languages)
	learned := make([]map[int]bool, m+1)
	for user, list := range languages {
		learned[user] = make(map[int]bool)
		for _, l := range list {
			learned[user][l] = true
		}
	}
	canTalk := make([][]bool, m+1)
	for i := range canTalk {
		canTalk[i] = make([]bool, m+1)
	}

	cnt := make([]int, n+1)
	needLearn := make(map[int]bool)

	for _, friends := range friendships {
		x, y := friends[0]-1, friends[1]-1
		for _, l := range languages[x] {
			if _, ok := learned[y][l]; ok {
				canTalk[x][y] = true
				break
			}
		}
		if !canTalk[x][y] {
			needLearn[x] = true
			needLearn[y] = true
		}
	}

	for x := range needLearn {
		for _, l := range languages[x] {
			cnt[l]++
		}
	}

	maxCommon := slices.Max(cnt)
	return len(needLearn) - maxCommon
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	languages := Deserialize[[][]int](ReadLine(stdin))
	friendships := Deserialize[[][]int](ReadLine(stdin))
	ans := minimumTeachings(n, languages, friendships)

	fmt.Println("\noutput:", Serialize(ans))
}
