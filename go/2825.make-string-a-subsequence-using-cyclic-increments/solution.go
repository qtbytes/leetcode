// Created by none at 2024/12/04 13:22
// leetgo: 1.4.9
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func canMakeSubsequence(str1 string, str2 string) bool {
	m, n := len(str1), len(str2)
	if m < n {
		return false
	}
	var i, j int
	for ; i < m && j < n; i++ {
		if str1[i] == str2[j] || (str1[i]+1-'a')%26 == (str2[j]-'a') {
			j++
		}
	}
	return j == n
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	str1 := Deserialize[string](ReadLine(stdin))
	str2 := Deserialize[string](ReadLine(stdin))
	ans := canMakeSubsequence(str1, str2)

	fmt.Println("\noutput:", Serialize(ans))
}
