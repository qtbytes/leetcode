// Created by none at 2024/09/27 13:00
// leetgo: 1.4.9
// https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func takeCharacters(s string, k int) (ans int) {
	cnt := []int{0, 0, 0}
	for _, ch := range s {
		cnt[ch-'a'] += 1
	}
	for i, c := range cnt {
		if c < k {
			return -1
		}
		// find s[l..r] have most `cnt - k` digit
		cnt[i] -= k
	}
	n := len(s)

	l := 0
	cur := []int{0, 0, 0}
	for r, ch := range s {
		key := ch - 'a'
		cur[key] += 1
		for cur[key] > cnt[key] {
			cur[s[l]-'a'] -= 1
			l += 1
		}
		// fmt.Println(cur, cnt, r, l)
		if r-l+1 > ans {
			ans = r - l + 1
		}
	}

	return n - ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	s := Deserialize[string](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := takeCharacters(s, k)

	fmt.Println("\noutput:", Serialize(ans))
}
