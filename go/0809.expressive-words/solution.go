// Created by none at 2025/08/25 16:17
// leetgo: dev
// https://leetcode.com/problems/expressive-words/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type Pair struct {
	ch   rune
	freq int
}

func count(s string) []Pair {
	i := 0
	n := len(s)
	res := make([]Pair, 0)
	for i < n {
		j := i + 1
		for j < n && s[j] == s[i] {
			j += 1
		}
		res = append(res, Pair{ch: rune(s[i]), freq: j - i})
		i = j
	}
	return res
}

func check(cur *[]Pair, target *[]Pair) bool {
	if len(*cur) != len(*target) {
		return false
	}
	for i := range *cur {
		p1, p2 := (*cur)[i], (*target)[i]
		if p1.ch != p2.ch || p1.freq > p2.freq {
			return false
		}
		if p1.freq < p2.freq && p2.freq <= 2 {
			return false
		}
	}
	return true
}

func expressiveWords(s string, words []string) int {
	target := count(s)
	res := 0

	for _, w := range words {
		cur := count(w)
		if check(&cur, &target) {
			res++
		}
	}

	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	s := Deserialize[string](ReadLine(stdin))
	words := Deserialize[[]string](ReadLine(stdin))
	ans := expressiveWords(s, words)

	fmt.Println("\noutput:", Serialize(ans))
}
