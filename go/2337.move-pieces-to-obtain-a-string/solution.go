// Created by none at 2024/12/05 14:26
// leetgo: 1.4.9
// https://leetcode.com/problems/move-pieces-to-obtain-a-string/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func canChange(start string, target string) bool {
	a := make([]int, 0, len(start))
	for i, ch := range start {
		if ch != '_' {
			a = append(a, i)
		}
	}
	b := make([]int, 0, len(start))
	for i, ch := range target {
		if ch != '_' {
			b = append(b, i)
		}
	}
	if len(a) != len(b) {
		return false
	}

	for i := range a {
		if start[a[i]] != target[b[i]] || (start[a[i]] == 'L' && a[i] < b[i]) || (start[a[i]] == 'R' && a[i] > b[i]) {
			return false
		}
	}
	return true
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	start := Deserialize[string](ReadLine(stdin))
	target := Deserialize[string](ReadLine(stdin))
	ans := canChange(start, target)

	fmt.Println("\noutput:", Serialize(ans))
}
