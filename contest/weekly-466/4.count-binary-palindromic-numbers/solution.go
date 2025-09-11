// Created by none at 2025/09/10 22:27
// leetgo: dev
// https://leetcode.com/problems/count-binary-palindromic-numbers/
// https://leetcode.com/contest/weekly-contest-466/problems/count-binary-palindromic-numbers/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
func dfs(n int64) int {
	if n == 0 {
		return 1
	}
	if n == 1 {
		return 2
	}
	s := fmt.Appendf(nil, "%b", n)
	m := len(s)
	for i := range (m + 1) / 2 {
		if s[i] != s[m-1-i] {
			if s[i] == '0' {
				s[m-1-i] = '0'
			} else {
				j := m - 1 - i
				for j >= i && s[j] == '0' {
					j--
				}
				s[j] = '0'
				j++
				for ; j < m; j++ {
					s[j] = '1'
				}
			}
		}
	}
	half := 0
	for i := 1; i < (m+1)/2; i++ {
		half = half<<1 | int(s[i]-'0')
	}
	res := 0
	if s[0] != '0' {
		res += (half + 1)
	}
	res += dfs(int64(1<<(m-1)) - 1)
	// fmt.Println(n, m, res)
	return res
}

func countBinaryPalindromes(n int64) int {
	return dfs(n)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int64](ReadLine(stdin))
	ans := countBinaryPalindromes(n)

	fmt.Println("\noutput:", Serialize(ans))
}
