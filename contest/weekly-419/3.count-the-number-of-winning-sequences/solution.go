// Created by none at 2024/10/13 15:11
// leetgo: 1.4.9
// https://leetcode.cn/problems/count-the-number-of-winning-sequences/
// https://leetcode.cn/contest/weekly-contest-419/problems/count-the-number-of-winning-sequences/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

const MOD = int(1e9) + 7

func countWinningSequences(s string) int {
	// F > E > W

	nums := make([]int, len(s))
	for i, ch := range s {
		switch ch {
		case 'F':
			nums[i] = 0
		case 'E':
			nums[i] = 1
		default:
			nums[i] = 2
		}
	}

	n := len(s)
	memo := make([][]map[int]int, n)
	for i := range n {
		memo[i] = make([]map[int]int, 4)
		for j := range 4 {
			memo[i][j] = make(map[int]int)
		}
	}
	var dfs func(i int, last int, score int) int
	dfs = func(i int, last int, score int) int {
		if i == n {
			if score > 0 {
				return 1
			}
			return 0
		}
		if x, ok := memo[i][last][score]; ok {
			return x
		}
		res := 0
		for cur := range 3 {
			if cur != last {
				d := cur - nums[i]
				var cur_score int
				if d == 0 {
					cur_score = 0
				} else if d == 1 || d == -2 {
					cur_score = -1
				} else if d == -1 || d == 2 {
					cur_score = 1
				}
				res += dfs(i+1, cur, score+cur_score)
			}
		}
		memo[i][last][score] = res % MOD
		return res % MOD
	}

	return dfs(0, 3, 0)

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	s := Deserialize[string](ReadLine(stdin))
	ans := countWinningSequences(s)

	fmt.Println("\noutput:", Serialize(ans))
}
