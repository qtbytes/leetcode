// Created by none at 2024/10/16 13:18
// leetgo: 1.4.9
// https://leetcode.cn/problems/longest-happy-string/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func longestDiverseString(a int, b int, c int) string {
	count := make(map[byte]int, 3)
	count['a'] = a
	count['b'] = b
	count['c'] = c
	res := []byte{}

	for n := 0; ; n++ {
		var key byte
		for ch, c := range count {
			if c > 0 && !(n >= 2 && ch == res[n-1] && ch == res[n-2]) {
				if key == 0 || c > count[key] {
					key = ch
				}
			}
		}
		if key == 0 {
			break
		}
		count[key]--
		res = append(res, key)
	}
	return string(res)

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	a := Deserialize[int](ReadLine(stdin))
	b := Deserialize[int](ReadLine(stdin))
	c := Deserialize[int](ReadLine(stdin))
	ans := longestDiverseString(a, b, c)

	fmt.Println("\noutput:", Serialize(ans))
}
