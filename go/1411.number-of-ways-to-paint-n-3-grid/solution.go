// Created by none at 2026/01/03 16:00
// leetgo: dev
// https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
const MOD int = 1e9 + 7

func numOfWays(n int) int {
	// actually: points only have 2 types:  aba, abc
	// aba has 3*2, g[aba] = {bab bac bcb cab cac} = aba * 3 + abc *2
	// abc has 3*2, {bab bca bcb cab}  = aba * 2 + abc*2
	f, g := 6, 6
	for range n - 1 {
		nf := (3*f + 2*g) % MOD
		ng := (2*f + 2*g) % MOD
		f, g = nf, ng
	}
	return (f + g) % MOD

	// points := [][3]int{}
	// for i := range 3 {
	// 	for j := range 3 {
	// 		if i == j {
	// 			continue
	// 		}
	// 		for k := range 3 {
	// 			if j == k {
	// 				continue
	// 			}
	// 			p := [3]int{i, j, k}
	// 			points = append(points, p)
	// 		}
	// 	}
	// }

	// g := make([][]int, len(points))
	// for i, x := range points {
	// 	for j, y := range points {
	// 		ok := func(x, y [3]int) bool {
	// 			for i := range x {
	// 				if x[i] == y[i] {
	// 					return false
	// 				}
	// 			}
	// 			return true
	// 		}
	// 		if x != y && ok(x, y) {
	// 			g[i] = append(g[i], j)
	// 		}
	// 	}
	// }

	// prev := make([]int, len(points))
	// for i := range prev {
	// 	prev[i] = 1
	// }
	// for range n - 1 {
	// 	next := make([]int, len(points))
	// 	for x, c := range prev {
	// 		for y := range g[x] {
	// 			next[y] = (next[y] + c) % MOD
	// 		}
	// 	}
	// 	prev = next
	// }

	// ans := 0
	// for _, x := range prev {
	// 	ans = (ans + x) % MOD
	// }
	// return ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	ans := numOfWays(n)

	fmt.Println("\noutput:", Serialize(ans))
}
