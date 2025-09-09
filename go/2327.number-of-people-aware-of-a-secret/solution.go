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
	// diff means how many people know secret in day i
	diff := make([]int, 2*n+1)
	diff[1] = 1
	diff[2] = -1
	d := 0
	res := 0
	for x := 1; x <= n; x++ {
		d = (d + diff[x]) % MOD
		if x+forget > n {
			res += d
		}
		diff[x+delay] += d
		diff[x+forget] -= d
	}
	return (res%MOD + MOD) % MOD
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
