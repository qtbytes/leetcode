// Created by none at 2025/09/28 15:24
// leetgo: dev
// https://leetcode.com/problems/number-of-zigzag-arrays-i/
// https://leetcode.com/contest/weekly-contest-469/problems/number-of-zigzag-arrays-i/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func zigZagArrays(n int, l int, r int) int {
	const mod int = 1e9 + 7
	// (l,r) => (0, r-l)
	m := r - l
	f := make([][]int, 2)
	prefix := make([][]int, 2)
	for i := range f {
		f[i] = make([]int, m+1)
		prefix[i] = make([]int, m+2)
		for j := range f[i] {
			f[i][j] = 1
			prefix[i][j+1] = j + 1
		}
	}

	for range n - 1 {
		g := make([][]int, 2)
		prefixNext := make([][]int, 2)
		for i := range g {
			g[i] = make([]int, m+1)
			prefixNext[i] = make([]int, m+2)
		}

		for x := range m + 1 {
			// g[x][0] = sum(f[1][:x])
			// g[x][1] = sum(f[0][x+1:])
			g[0][x] = prefix[1][x]
			prefixNext[0][x+1] = (prefixNext[0][x] + g[0][x]) % mod
			g[1][x] = (prefix[0][m+1] - prefix[0][x+1] + mod) % mod
			prefixNext[1][x+1] = (prefixNext[1][x] + g[1][x]) % mod
		}
		f = g
		prefix = prefixNext
		// fmt.Println(f)
	}

	res := 0
	for _, row := range f {
		for _, x := range row {
			res += x
		}
	}
	return res % mod
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	l := Deserialize[int](ReadLine(stdin))
	r := Deserialize[int](ReadLine(stdin))
	ans := zigZagArrays(n, l, r)

	fmt.Println("\noutput:", Serialize(ans))
}
