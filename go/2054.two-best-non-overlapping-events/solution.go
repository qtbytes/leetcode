// Created by none at 2024/12/08 14:42
// leetgo: 1.4.9
// https://leetcode.com/problems/two-best-non-overlapping-events/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maxTwoEvents(events [][]int) int {
	sort.Slice(events, func(i, j int) bool {
		return events[i][1] < events[j][1]
	})
	q := []int{}
	score := make(map[int]int)
	res := 0
	for _, e := range events {
		start, end, value := e[0], e[1], e[2]
		i := sort.Search(len(q), func(i int) bool {
			return q[i] >= start
		})
		cur := value
		if len(q) == 0 || cur > score[q[len(q)-1]] {
			q = append(q, end)
		}
		score[end] = max(score[end], value)
		if i-1 >= 0 {
			cur += score[q[i-1]]
		}
		res = max(res, cur)
	}
	// fmt.Println(q, score)
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	events := Deserialize[[][]int](ReadLine(stdin))
	ans := maxTwoEvents(events)

	fmt.Println("\noutput:", Serialize(ans))
}
