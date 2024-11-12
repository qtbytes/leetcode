// Created by none at 2024/11/12 13:42
// leetgo: 1.4.9
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maximumBeauty(items [][]int, queries []int) []int {
	// sort items + binary search
	// or sort items and queries
	best_items := make(map[int]int)
	for _, item := range items {
		p, b := item[0], item[1]
		best_items[p] = max(best_items[p], b)
	}

	keys := make([]int, 0, len(best_items))
	for k := range best_items {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	q := make([][]int, 0, len(best_items))
	for _, k := range keys {
		v := best_items[k]
		if len(q) == 0 || v > q[len(q)-1][1] {
			q = append(q, []int{k, v})
		}
	}

	ans := make([]int, len(queries))
	for i, price := range queries {
		j := sort.Search(len(q), func(i int) bool {
			return q[i][0] > price
		})
		if j > 0 {
			ans[i] = q[j-1][1]
		}
	}
	return ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	items := Deserialize[[][]int](ReadLine(stdin))
	queries := Deserialize[[]int](ReadLine(stdin))
	ans := maximumBeauty(items, queries)

	fmt.Println("\noutput:", Serialize(ans))
}
