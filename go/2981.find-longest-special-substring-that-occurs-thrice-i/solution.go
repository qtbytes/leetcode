// Created by none at 2024/12/10 15:14
// leetgo: 1.4.9
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maximumLength(s string) int {
	cnt := make([][]int, 26)
	n := len(s)
	for i := 0; i < n; {
		j := i + 1
		for j < n && s[i] == s[j] {
			j++
		}
		cnt[s[i]-'a'] = append(cnt[s[i]-'a'], j-i)
		i = j
	}
	ans := 0
	for _, v := range cnt {
		sort.Slice(v, func(i, j int) bool {
			return v[i] < v[j]
		})
		m := len(v)
		if m >= 3 && v[m-3] == v[m-1] {
			ans = max(ans, v[m-1])
		}
		if m >= 2 && v[m-2] >= v[m-1]-1 {
			ans = max(ans, v[m-1]-1)
		}
		if m >= 1 && v[m-1] >= 3 {
			ans = max(ans, v[m-1]-2)
		}
	}
	if ans > 0 {
		return ans
	}
	return -1
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	s := Deserialize[string](ReadLine(stdin))
	ans := maximumLength(s)

	fmt.Println("\noutput:", Serialize(ans))
}
