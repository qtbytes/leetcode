// Created by none at 2025/08/26 15:40
// leetgo: dev
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func balancedString(s string) int {
	n := len(s)
	cnt := make(map[rune]int)
	for _, ch := range s {
		cnt[ch]++
	}

	valid := func() bool {
		for _, v := range cnt {
			if v > n/4 {
				return false
			}
		}
		return true
	}

	res := 1 << 31
	r := 0

	for l, ch := range s {
		for r < n && !valid() {
			cnt[rune(s[r])]--
			r++
		}
		// delete [l..r]
		if valid() {
			res = min(res, r-l)
		} else {
			break
		}
		cnt[ch]++
	}

	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	s := Deserialize[string](ReadLine(stdin))
	ans := balancedString(s)

	fmt.Println("\noutput:", Serialize(ans))
}
