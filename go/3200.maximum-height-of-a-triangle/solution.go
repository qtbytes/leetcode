// Created by none at 2024/10/15 10:55
// leetgo: 1.4.9
// https://leetcode.cn/problems/maximum-height-of-a-triangle/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func helper(a, b int) int {
	for i := 1; ; i++ {
		if i&1 == 0 {
			b -= i
			if b < 0 {
				return i - 1
			}
		} else {
			a -= i
			if a < 0 {
				return i - 1
			}
		}
	}
}
func maxHeightOfTriangle(red int, blue int) int {
	return max(helper(red, blue), helper(blue, red))
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	red := Deserialize[int](ReadLine(stdin))
	blue := Deserialize[int](ReadLine(stdin))
	ans := maxHeightOfTriangle(red, blue)

	fmt.Println("\noutput:", Serialize(ans))
}
