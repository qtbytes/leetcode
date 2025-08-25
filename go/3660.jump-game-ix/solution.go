// Created by none at 2025/08/25 22:51
// leetgo: dev
// https://leetcode.com/problems/jump-game-ix/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type Pair struct {
	x     int
	value int
}

func maxValue(nums []int) []int {
	n := len(nums)
	res := make([]int, n)
	left_max := make([]int, n)
	x := 0
	for i, y := range nums {
		x = max(x, y)
		left_max[i] = x
	}

	st := make([]Pair, 0)

	for i := n - 1; i >= 0; i-- {
		// fmt.Println(st)
		res[i] = left_max[i]
		j := sort.Search(len(st), func(j int) bool { return st[j].x < res[i] })
		if j < len(st) {
			res[i] = max(res[i], st[j].value)
		}
		for len(st) > 0 {
			p := st[len(st)-1]
			if nums[i] <= p.x && res[i] >= p.value {
				st = st[:len(st)-1]
			} else {
				break
			}
		}
		if len(st) == 0 || nums[i] < st[len(st)-1].x || res[i] < st[len(st)-1].value {
			st = append(st, Pair{nums[i], res[i]})
		}
	}

	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := maxValue(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
