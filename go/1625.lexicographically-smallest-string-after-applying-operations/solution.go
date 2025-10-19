// Created by none at 2025/10/19 19:08
// leetgo: dev
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
func change(x int, y int) int {
	add := 0
	pre := x
	for i := range 10 {
		cur := (x + y*i) % 10
		if cur < pre {
			pre = cur
			add = y * i
		}
	}
	return add
}

func findLexSmallestString(s string, a int, b int) string {
	n := len(s)
	res := strings.Repeat("9", n)
	visited := make(map[int]bool)
	if b&1 == 0 {
		for i := 0; ; i = (i - b + n) % n {
			if visited[i] {
				break
			}
			visited[i] = true
			if s[i] > res[0] {
				continue
			}
			var t []byte
			x := change(int(s[(i+1)%n]-'0'), a)

			for j := range n {
				k := (i + j) % n
				if k&1 == 0 {
					t = append(t, s[k])
				} else {
					char := (int(s[k]-'0') + x) % 10
					t = append(t, byte(char+'0'))
				}
			}
			res = min(res, string(t))
			// fmt.Println(i, res, string(t))
		}
		return res
	}
	for i := 0; ; i = (i - b + n) % n {
		if visited[i] {
			break
		}
		visited[i] = true
		var t []byte
		x0 := change(int(s[i]-'0'), a)
		x1 := change(int(s[(i+1)%n]-'0'), a)

		for j := range n {
			k := (i + j) % n
			var char int
			if k&1 == i&1 {
				char = (int(s[k]-'0') + x0) % 10
			} else {
				char = (int(s[k]-'0') + x1) % 10
			}
			t = append(t, byte(char+'0'))
		}
		// fmt.Println(string(t), i, x0, x1)
		res = min(res, string(t))
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	s := Deserialize[string](ReadLine(stdin))
	a := Deserialize[int](ReadLine(stdin))
	b := Deserialize[int](ReadLine(stdin))
	ans := findLexSmallestString(s, a, b)

	fmt.Println("\noutput:", Serialize(ans))
}
