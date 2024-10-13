// Created by none at 2024/10/13 11:24
// leetgo: 1.4.9
// https://leetcode.cn/problems/egg-drop-with-2-eggs-and-n-floors/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func twoEggDrop(n int) int {
	res := 0
	cnt := 1
	for n > 0 {
		res = max(res, cnt)
		n -= cnt
		cnt += 1
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	ans := twoEggDrop(n)

	fmt.Println("\noutput:", Serialize(ans))
}
