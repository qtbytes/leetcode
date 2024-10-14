// Created by none at 2024/10/14 11:47
// leetgo: 1.4.9
// https://leetcode.cn/problems/super-egg-drop/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func superEggDrop(k int, n int) int {

	var dfs func(k, n int) int
	memo := make([][]int, k+1)
	for i := range k + 1 {
		memo[i] = make([]int, n+1)
	}

	dfs = func(k, n int) int {
		if k == 1 {
			return n
		}
		if n <= 2 {
			return n
		}
		if memo[k][n] != 0 {
			return memo[k][n]
		}

		// res := n
		// for j := 2; j <= (n+2)/2; j++ {
		// 	res = min(res, 1+max(dfs(k-1, j-1), dfs(k, n-j)))
		// }

		// As j gets bigger, dfs(k-1,j-1) gets bigger and dfs(k, n-j) gets smaller.
		// Therefore, we get minimal dfs(k,j) when dfs(k-1,j-1) == dfs(k,n-j)
		l, r := 1, n
		for l < r {
			mid := (l + r) >> 1
			if dfs(k-1, mid-1) <= dfs(k, n-mid) {
				l = mid + 1
			} else {
				r = mid
			}
		}
		j := l
		res := 1 + max(dfs(k-1, j-1), dfs(k, n-j))
		res = min(res, 1+max(dfs(k-1, j-2), dfs(k, n-j+1)))

		memo[k][n] = res
		return res
	}
	return dfs(k, n)

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	k := Deserialize[int](ReadLine(stdin))
	n := Deserialize[int](ReadLine(stdin))
	ans := superEggDrop(k, n)

	fmt.Println("\noutput:", Serialize(ans))
}
