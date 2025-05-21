// Created by none at 2025/05/21 15:33
// leetgo: dev
// https://leetcode.com/problems/alien-dictionary/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type Pair struct {
	x, y int
}

func alienOrder(words []string) string {
	g := make(map[int][]int, 26)
	visited := make(map[Pair]bool)
	deg := make(map[int]int, 26)
	n := len(words)
	for i := range words {
		for _, ch := range words[i] {
			deg[int(ch-'a')] += 0
		}
		j := i + 1
		if j == n {
			continue
		}
		if len(words[i]) > len(words[j]) && strings.HasPrefix(words[i], words[j]) {
			return ""
		}
		for k := range min(words[i], words[j]) {
			x, y := int(words[i][k]-'a'), int(words[j][k]-'a')
			if x != y {
				if !visited[Pair{x, y}] {
					visited[Pair{x, y}] = true
					deg[y] += 1
					g[x] = append(g[x], y)
				}
				break
			}
		}
	}

	q := make([]int, 0)
	for i, d := range deg {
		if d == 0 {
			q = append(q, i)
		}
	}
	res := make([]rune, 0)
	for len(q) > 0 {
		x := q[0]
		q = q[1:]
		res = append(res, rune(x+'a'))
		for _, y := range g[x] {
			deg[y] -= 1
			if deg[y] == 0 {
				q = append(q, y)
			}
		}
	}
	if len(res) == len(deg) {
		return string(res)
	}
	return ""

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	words := Deserialize[[]string](ReadLine(stdin))
	ans := alienOrder(words)

	fmt.Println("\noutput:", Serialize(ans))
}
