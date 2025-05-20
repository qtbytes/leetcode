// Created by none at 2025/05/20 14:49
// leetgo: dev
// https://leetcode.com/problems/find-longest-self-contained-substring/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maxSubstringLength(s string) int {
	first := make([]int, 26)
	last := make([]int, 26)
	for i := range first {
		first[i] = -1
		last[i] = -1
	}
	for i, ch := range s {
		index := ch - 'a'
		if first[index] == -1 {
			first[index] = i
		}
		last[index] = i
	}

	res := -1
	for x, start := range first {
		if start == -1 {
			continue
		}
		end := last[x]
		for i := start; i < len(s); i++ {
			y := int(s[i] - 'a')
			if first[y] < start {
				break
			}
			end = max(end, last[y])
			if end == i && end-start+1 != len(s) {
				res = max(res, end-start+1)
			}
		}
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	s := Deserialize[string](ReadLine(stdin))
	ans := maxSubstringLength(s)

	fmt.Println("\noutput:", Serialize(ans))
}
