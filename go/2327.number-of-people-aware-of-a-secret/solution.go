// Created by none at 2025/09/09 10:18
// leetgo: dev
// https://leetcode.com/problems/number-of-people-aware-of-a-secret/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
const MOD = int(1e9) + 7

func peopleAwareOfSecret(n int, delay int, forget int) int {
	diff := make([]int, 2*n+1)
	diff[1] = 1
	d := 0
	for x := 1; x <= n; x++ {
		if diff[x] > 0 {
			for y := x + delay; y < x+forget; y++ {
				diff[y] = (diff[y] + diff[x]) % MOD
			}
			if x+forget <= n {
				// will forget
			} else {
				d += diff[x]
			}
		}
	}
	return d % MOD
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	delay := Deserialize[int](ReadLine(stdin))
	forget := Deserialize[int](ReadLine(stdin))
	ans := peopleAwareOfSecret(n, delay, forget)

	fmt.Println("\noutput:", Serialize(ans))
}
