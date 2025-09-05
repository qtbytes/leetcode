// Created by none at 2025/09/05 12:01
// leetgo: dev
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
var N = 62

func makeTheIntegerZero(num1 int, num2 int) int {
	if num2 == 0 {
		return bits.OnesCount(uint(num1))
	}
	// enumerate times
	for x := 1; x <= N; x++ {
		num1 := num1 - num2*x
		if num1 < x && num2 > 0 {
			break
		}
		// fmt.Println(num1)
		if x >= bits.OnesCount(uint(num1)) {
			return x
		}
	}
	return -1
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	num1 := Deserialize[int](ReadLine(stdin))
	num2 := Deserialize[int](ReadLine(stdin))
	ans := makeTheIntegerZero(num1, num2)

	fmt.Println("\noutput:", Serialize(ans))
}
