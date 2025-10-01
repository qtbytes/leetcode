// Created by none at 2025/10/01 12:20
// leetgo: dev
// https://leetcode.com/problems/water-bottles/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func numWaterBottles(numBottles int, numExchange int) int {
	res := 0
	for numBottles >= numExchange {
		n := numBottles / numExchange
		res += n * numExchange
		numBottles = numBottles%numExchange + n
	}
	return res + numBottles
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	numBottles := Deserialize[int](ReadLine(stdin))
	numExchange := Deserialize[int](ReadLine(stdin))
	ans := numWaterBottles(numBottles, numExchange)

	fmt.Println("\noutput:", Serialize(ans))
}
